from models.person import Person
from models.student import Student
from models.librarian import Librarian, AccessLevel
from utils.generate_id import generate_id
from models.book import Book
from models.borrow_record import BorrowRecord
from datetime import date, timedelta
from models.library import Library

def main():
    # 1. Create a library instance
    library = Library("Central Library")
    print(f"Created library: {library.name}")

    # 2. Create and add a book
    book1 = Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J.K. Rowling",
        isbn="9780747532699",
        genre="Fantasy",
        publication_year=1997,
        copies_available=3,
        total_copies=3
    )
    library.add_book(book1)
    print(f"Added book: {book1.title}")

    # 3. Register a student
    student1 = Student(
        name="John",
        surname="Doe",
        id="S001",
        email="john.doe@example.com",
        major="Computer Science",
        year=2
    )
    library.register_student(student1)
    print(f"Registered student: {student1.name} {student1.surname}")

    # 4. Register a librarian
    librarian1 = Librarian(
        name="Jane",
        surname="Smith",
        id="L001",
        email="jane.smith@example.com",
        access_level=AccessLevel.ADMIN.value
    )
    library.register_librarian(librarian1)
    print(f"Registered librarian: {librarian1.name} {librarian1.surname}")

    # 5. Borrow a book
    borrow_date = date.today()
    due_date = borrow_date + timedelta(days=14)
    record = library.borrow_book(student_id=student1.person_id, isbn=book1.isbn, borrow_date=borrow_date, due_date=due_date)
    print(f"{student1.name} borrowed '{book1.title}' on {borrow_date}")

    # 6. Return the book
    return_date = borrow_date + timedelta(days=16) 
    library.return_book(student_id=student1.person_id, isbn=book1.isbn, return_date=return_date)
    print(f"{student1.name} returned '{book1.title}' on {return_date}")

    # 7. Generate and print a report
    report = library.generate_report()
    print("\nLibrary Report:")
    print(report)

if __name__ == "__main__":
    main()