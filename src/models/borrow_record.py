import uuid
from datetime import datetime, timedelta

class BorrowRecord:
    FINE_PER_DAY = 1.0
    MAX_FINE = 100.0

    def __init__(self, student, book, borrow_date=None, due_days=14):
        self.__record_id = str(uuid.uuid4())
        self.__student = student
        self.__book = book
        self.__borrow_date = borrow_date or datetime.today().date()
        self.__due_date = self.__borrow_date + timedelta(days=due_days)
        self.__return_date = None
        self.__fine_amount = 0.0
    
    @property
    def record_id(self):
        return self.__record_id

    @property
    def student(self):
        return self.__student

    @property
    def book(self):
        return self.__book

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def return_date(self):
        return self.__return_date

    @property
    def fine_amount(self):
        return self.__fine_amount

    # --- Mark as returned ---
    def mark_returned(self, return_date=None):
        self.__return_date = return_date or datetime.today().date()
        self.__fine_amount = self.calculate_fine(self.__return_date)

    # --- Check if overdue ---
    def is_overdue(self, on_date=None):
        today = on_date or datetime.today().date()
        return today > self.__due_date and self.__return_date is None

    # --- Fine calculation ---
    def calculate_fine(self, return_date):
        if return_date <= self.__due_date:
            return 0.0
        days_late = (return_date - self.__due_date).days
        fine = days_late * self.FINE_PER_DAY
        return min(fine, self.MAX_FINE)

    # --- Static config ---
    @staticmethod
    def set_fine_per_day(amount):
        BorrowRecord.FINE_PER_DAY = amount

    @staticmethod
    def set_max_fine(cap):
        BorrowRecord.MAX_FINE = cap

    def __str__(self):
        return (f"BorrowRecord(ID: {self.record_id}, "
                f"Student: {self.student.full_name}, "
                f"Book: {self.book.title}, "
                f"Borrowed: {self.borrow_date}, Due: {self.due_date}, "
                f"Returned: {self.return_date or 'Not returned'}, "
                f"Fine: {self.fine_amount})")