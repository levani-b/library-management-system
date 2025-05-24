import re
from datetime import datetime


class Book:
    def __init__(self, isbn, title, author, genre, publication_year, total_copies):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_year = publication_year
        self.__total_copies = total_copies
        self.__copies_available = total_copies
    
    # --- ISBN ---
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        pattern = r"^(97(8|9))?\d{9}(\d|X)$"
        if not re.match(pattern, value.replace("-", "").replace(" ", "")):
            raise ValueError("Invalid ISBN format")
        self.__isbn = value

    # --- Title ---
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self.__title = value

    # --- Author ---
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Author name cannot be empty")
        self.__author = value

    # --- Genre ---
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    # --- Publication Year ---
    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        now = datetime.now()
        current_year = now.year
        if not isinstance(value, int) or value < 1000 or value > current_year + 1:
            raise ValueError(f"Publication year must be between 1000 and {current_year + 1}")
        self.__publication_year = value
    
     # --- Total Copies ---
    @property
    def total_copies(self):
        return self.__total_copies

    @total_copies.setter
    def total_copies(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Total copies must be a non-negative integer")
        if hasattr(self, '_Book__copies_available') and value < self.__copies_available:
            self.__copies_available = value
        self.__total_copies = value

    # --- Copies Available ---
    @property
    def copies_available(self):
        return self.__copies_available

    @copies_available.setter
    def copies_available(self, value):
        if not 0 <= value <= self.total_copies:
            raise ValueError("Available copies must be between 0 and total copies")
        self.__copies_available = value

    # --- Methods ---
    def is_available(self):
        return self.copies_available > 0

    def borrow_copy(self):
        if self.copies_available <= 0:
            raise Exception("No copies available to borrow")
        self.copies_available -= 1

    def return_copy(self):
        if self.copies_available >= self.total_copies:
            raise Exception("All copies are already returned")
        self.copies_available += 1

    # --- Comparison for sorting ---
    def __lt__(self, other):
        return self.title < other.title

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __str__(self):
        return (f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
                f"Genre: {self.genre}, Year: {self.publication_year}, "
                f"Available: {self.copies_available}/{self.total_copies})")