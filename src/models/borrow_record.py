import uuid
from datetime import date
from models.student import Student
from models.book import Book

class BorrowRecord:
    DAILY_FINE = 0.5 

    def __init__(self, student, book, borrow_date, due_date, return_date=None, fine_amount=0.0):
        self.__record_id = self.__generate_record_id()
        self.__student = self.__validate_student(student)
        self.__book = self.__validate_book(book)
        self.__borrow_date = self.__validate_date(borrow_date)
        self.__due_date = self.__validate_date(due_date)
        self.__return_date = self.__validate_date(return_date) if return_date else None
        self.__fine_amount = self.__validate_fine(fine_amount)

    def __generate_record_id(self):
        return str(uuid.uuid4())

    def __validate_student(self, value):
        if not isinstance(value, Student):
            raise TypeError("student must be a Student instance")
        return value

    def __validate_book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be a Book instance")
        return value

    def __validate_date(self, value):
        if value is not None and not isinstance(value, date):
            raise TypeError("date must be a datetime.date instance or None")
        return value

    def __validate_fine(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("fine_amount must be a number")
        if value < 0:
            raise ValueError("fine_amount cannot be negative")
        return float(value)

    @property
    def record_id(self):
        return self.__record_id

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = self.__validate_student(value)

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        self.__book = self.__validate_book(value)

    @property
    def borrow_date(self):
        return self.__borrow_date

    @borrow_date.setter
    def borrow_date(self, value):
        self.__borrow_date = self.__validate_date(value)

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = self.__validate_date(value)

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self, value):
        self.__return_date = self.__validate_date(value)

    @property
    def fine_amount(self):
        return self.__fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self.__fine_amount = self.__validate_fine(value)

    def is_overdue(self):
        if self.__return_date is not None:
            compare_date = self.__return_date
        else:
            compare_date = date.today()
        if compare_date > self.__due_date:
            return True
        else:
            return False

    def days_overdue(self):
        if self.__return_date is not None:
            compare_date = self.__return_date
        else:
            compare_date = date.today()
        if compare_date > self.__due_date:
            delta = compare_date - self.__due_date
            return delta.days
        else:
            return 0

    def calculate_fine(self):
        days = self.days_overdue()
        fine = self.fine_rule(days)
        return fine

    @staticmethod
    def fine_rule(days_overdue):
        if days_overdue > 0:
            return days_overdue * BorrowRecord.DAILY_FINE
        else:
            return 0.0

    def update_fine(self):
        fine = self.calculate_fine()
        self.__fine_amount = fine

    def mark_returned(self, return_date):
        validated_date = self.__validate_date(return_date)
        self.__return_date = validated_date
        self.update_fine()

    def __str__(self):
        return (f"RecordID: {self.__record_id} | Student: {self.__student} | Book: {self.__book} | "
                f"Borrowed: {self.__borrow_date} | Due: {self.__due_date} | "
                f"Returned: {self.__return_date} | Fine: {self.__fine_amount:.2f}")