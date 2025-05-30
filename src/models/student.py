import re
from models.person import Person

class Student(Person):
    def __init__(self, first_name, last_name, email, phone, person_id, major, year):
        super().__init__(first_name, last_name, email, phone, person_id)
        self.__major = major
        self.__year = year
        self.__borrowed_books = []
        self.__borrowing_history = []
    
    # --- Major --
    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self,value):
        if not value.strip():
            raise ValueError("Major cannot be empty")
        self.__major = value
    
    # --- Year ---
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 1 or value > 6:
            raise ValueError("Year must be an integer between 1 and 6.")
        self.__year = value
    
    # --- Borrowed Books and Borrowing History ---
    @property
    def borrowed_books(self):
        return self.__borrowed_books.copy()

    @property
    def borrowing_history(self):
        return self.__borrowing_history.copy()
    
    def add_borrowed_book(self, book):
        self.__borrowed_books.append(book)
    
    def remove_borrowed_book(self, book):
        if len(self.__borrowed_books) <= 0:
            return "There are not borrowed books"
        self.__borrowed_books.remove(book)

    def add_to_history(self, record):
        self.__borrowing_history.append(record)
    
    def __str__(self):
        return f"Student(Name: {self.full_name}, ID: {self.person_id}, Major: {self.__major}, Year: {self.__year}, Email: {self.email})"