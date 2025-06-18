from models.person import Person
from models.student import Student
from models.librarian import Librarian, AccessLevel
from utils.generate_id import generate_id
from models.book import Book
from models.borrow_record import BorrowRecord
from datetime import date, timedelta

def main():
    # Create a student
    student = Student(
        name="Harry",
        surname="Potter",
        id=generate_id(name="Harry", surname="Potter"),
        email="harry.potter@hogwarts.edu",
        major="Magic",
        year=3
    )

    # Create a book
    book = Book(
        title="Advanced Potion Making",
        author="Libatius Borage",
        isbn="9876543210",
        genre="Magic",
        publication_year=1946,
        copies_available=1,
        total_copies=1
    )

    # Simulate borrowing the book
    borrow_date = date.today()
    due_date = borrow_date + timedelta(days=14)

    # Create a borrow record
    record = BorrowRecord(
        student=student,
        book=book,
        borrow_date=borrow_date,
        due_date=due_date
    )

    print("Student:", student)
    print("Book:", book)
    print("Borrow Record:", record)

    # Simulate returning the book late
    return_date = due_date + timedelta(days=5)
    record.mark_returned(return_date)

    print("\nAfter returning the book late:")
    print("Borrow Record:", record)
    print("Is overdue?", record.is_overdue())
    print("Days overdue:", record.days_overdue())
    print("Fine amount:", record.fine_amount)

if __name__ == "__main__":
    main()