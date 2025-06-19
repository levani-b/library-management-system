from models.student import Student
from models.librarian import Librarian
from models.book import Book
from models.borrow_record import BorrowRecord

class Library:
    def __init__(self,name):
        self.__name = self.__validate_name(name)
        self.__books = {}
        self.__students = {}
        self.__librarians = {}
        self.__borrow_records = []
    
    def __validate_name(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if not value:
            raise ValueError('Name cannot be empty')
        return value.title()
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = self.__validate_name(value)
    
    @property
    def books(self):
        return self.__books

    @property
    def students(self):
        return self.__students

    @property
    def librarians(self):
        return self.__librarians

    @property
    def borrow_records(self):
        return self.__borrow_records

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        isbn = book.isbn
        if isbn in self.__books:
            existing_book = self.__books[isbn]
            existing_book.total_copies += book.total_copies
            existing_book.copies_available += book.copies_available
        else:
            self.__books[isbn] = book

    def remove_book(self, isbn):
        if isbn not in self.__books:
            raise KeyError(f"No book with ISBN {isbn} found in the library.")
        del self.__books[isbn]

    def search_books(self, query, field="title"):
        if field not in ("title", "author", "genre"):
            raise ValueError("Search field must be 'title', 'author', or 'genre'.")
        query = query.strip().lower()
        results = []
        for book in self.__books.values():
            value = getattr(book, field, None)
            if value and query in value.lower():
                results.append(book)
        return results

    def register_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("student must be a Student instance")
        student_id = student.person_id
        if student_id in self.__students:
            raise ValueError(f"Student with ID {student_id} is already registered.")
        self.__students[student_id] = student

    def register_librarian(self, librarian):
        if not isinstance(librarian, Librarian):
            raise TypeError("librarian must be a Librarian instance")
        librarian_id = librarian.person_id
        if librarian_id in self.__librarians:
            raise ValueError(f"Librarian with ID {librarian_id} is already registered.")
        self.__librarians[librarian_id] = librarian

    def borrow_book(self, student_id, isbn, borrow_date, due_date):
        if student_id not in self.__students:
            raise KeyError(f"No student with ID {student_id} found.")
        if isbn not in self.__books:
            raise KeyError(f"No book with ISBN {isbn} found.")
        student = self.__students[student_id]
        book = self.__books[isbn]
        if not book.is_available():
            raise ValueError(f"Book '{book.title}' is not available for borrowing.")
        if book in student.borrowed_books:
            raise ValueError(f"Student already borrowed this book.")
        
        book.borrow_copy()
        student.borrow_book(book)
        record = BorrowRecord(student, book, borrow_date, due_date)
        self.__borrow_records.append(record)
        return record

    def return_book(self, student_id, isbn, return_date):
        if student_id not in self.__students:
            raise KeyError(f"No student with ID {student_id} found.")
        if isbn not in self.__books:
            raise KeyError(f"No book with ISBN {isbn} found.")
        student = self.__students[student_id]
        book = self.__books[isbn]
        if book not in student.borrowed_books:
            raise ValueError(f"Student did not borrow this book.")
        book.return_book_copy()
        student.return_book(book)
        for record in reversed(self.__borrow_records):
            if (record.student == student and record.book == book and record.return_date is None):
                record.mark_returned(return_date)
                break
        else:
            raise ValueError("No active borrow record found for this student and book.")

    def get_overdue_books(self):
        overdue_records = []
        for record in self.__borrow_records:
            if record.is_overdue() and record.return_date is None:
                overdue_records.append(record)
        return overdue_records

    def generate_report(self):
        report = []
        report.append(f"Library Name: {self.name}")
        report.append(f"Total Books: {len(self.__books)}")
        report.append(f"Total Students: {len(self.__students)}")
        report.append(f"Total Librarians: {len(self.__librarians)}")
        report.append(f"Total Borrow Records: {len(self.__borrow_records)}")
        overdue = self.get_overdue_books()
        report.append(f"Overdue Books: {len(overdue)}")
        return "\n".join(report)

    def save_data(self, books_file, students_file, records_file):
        from utils.file_handler import save_json
        books_list = []
        for book in self.__books.values():
            books_list.append(self._serialize_book(book))
        save_json(books_file, books_list)

        students_list = []
        for student in self.__students.values():
            students_list.append(self._serialize_student(student))
        save_json(students_file, students_list)

        records_list = []
        for record in self.__borrow_records:
            records_list.append(self._serialize_borrow_record(record))
        save_json(records_file, records_list)

    def load_data(self, books_file, students_file, records_file):
        from utils.file_handler import load_json
        from models.book import Book
        from models.student import Student
        from models.borrow_record import BorrowRecord
        books_data = load_json(books_file)
        students_data = load_json(students_file)
        records_data = load_json(records_file)

        self.__books = {}
        for b in books_data:
            book = Book(**b)
            self.__books[book.isbn] = book

        self.__students = {}
        for s in students_data:
            student = Student(**s)
            self.__students[student.person_id] = student

        self.__borrow_records = []
        for r in records_data:
            record = BorrowRecord(**r)
            self.__borrow_records.append(record)

    def _serialize_book(self, book):
        return {
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'genre': book.genre,
            'publication_year': book.publication_year,
            'copies_available': book.copies_available,
            'total_copies': book.total_copies
        }

    def _serialize_student(self, student):
        return {
            'name': student.name,
            'surname': student.surname,
            'person_id': student.person_id,
            'email': student.email,
            'major': student.major,
            'year': student.year
        }

    def _serialize_borrow_record(self, record):
        return {
            'record_id': record.record_id,
            'student': record.student.person_id,
            'book': record.book.isbn,
            'borrow_date': record.borrow_date.isoformat() if record.borrow_date else None,
            'due_date': record.due_date.isoformat() if record.due_date else None,
            'return_date': record.return_date.isoformat() if record.return_date else None,
            'fine_amount': record.fine_amount
        }
        