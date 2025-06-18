class Book:
    def __init__(self, title, author, isbn, genre, publication_year, copies_available=1, total_copies=1):
        self.__title = self.__validate_title(title)
        self.__author = self.__validate_author(author)
        self.__isbn = self.__validate_isbn(isbn)
        self.__genre = self.__validate_genre(genre)
        self.__publication_year = self.__validate_publication_year(publication_year)
        self.__copies_available = self.__validate_copies(copies_available)
        self.__total_copies = self.__validate_copies(total_copies)

    def __validate_title(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Title must be a string')
        if not value:
            raise ValueError('Title cannot be empty')
        return value.title()

    def __validate_author(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Author must be a string')
        if not value:
            raise ValueError('Author cannot be empty')
        return value.title()

    def __validate_isbn(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('ISBN must be a string')
        if not value:
            raise ValueError('ISBN cannot be empty')
        if not (len(value) == 10 or len(value) == 13) or not value.isdigit():
            raise ValueError('ISBN must be a 10 or 13 digit number')
        return value

    def __validate_genre(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Genre must be a string')
        if not value:
            raise ValueError('Genre cannot be empty')
        return value.title()

    def __validate_publication_year(self, value):
        if not isinstance(value, int):
            raise TypeError('Publication year must be an integer')
        if value < 0 or value > 2100:
            raise ValueError('Publication year must be a valid year')
        return value

    def __validate_copies(self, value):
        if not isinstance(value, int):
            raise TypeError('Copies must be an integer')
        if value < 0:
            raise ValueError('Copies cannot be negative')
        return value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = self.__validate_title(value)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = self.__validate_author(value)

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = self.__validate_isbn(value)

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = self.__validate_genre(value)

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        self.__publication_year = self.__validate_publication_year(value)

    @property
    def copies_available(self):
        return self.__copies_available

    @copies_available.setter
    def copies_available(self, value):
        self.__copies_available = self.__validate_copies(value)

    @property
    def total_copies(self):
        return self.__total_copies

    @total_copies.setter
    def total_copies(self, value):
        self.__total_copies = self.__validate_copies(value)

    def is_available(self):
        return self.__copies_available > 0

    def borrow_copy(self):
        if self.__copies_available > 0:
            self.__copies_available -= 1
            return True
        return False

    def return_book_copy(self):
        if self.__copies_available < self.__total_copies:
            self.__copies_available += 1
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__isbn == other.__isbn

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.__title < other.__title

    def __str__(self):
        return (f"{self.__title} by {self.__author} | ISBN: {self.__isbn} | Genre: {self.__genre} | "
                f"Year: {self.__publication_year} | Available: {self.__copies_available}/{self.__total_copies}")
    