from models.person import Person

class Student(Person):
    def __init__(self, name, surname, id, email, major, year):
        super().__init__(name, surname, id, email)
        self.__major = self.__validate_major(major)
        self.__year = self.__validate_year(year)
        self.__borrowed_books = []
        self.__borrowing_history = []

    def __validate_major(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Major must be string')
        if value == '':
            raise ValueError('Major can not be empty')
        if len(value) < 2:
            raise ValueError('Major must be at least 2 characters long')
        return value.title()

    def __validate_year(self, value):
        if not isinstance(value, int):
            raise TypeError('Year must be integer')
        if value < 1 or value > 4:
            raise ValueError('Year must be between 1 and 4')
        return value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = self.__validate_major(value)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = self.__validate_year(value)

    def borrow_book(self, book):
        if book in self.__borrowed_books:
            raise ValueError('Book is already borrowed')
        self.__borrowed_books.append(book)
        self.__borrowing_history.append(book)

    def return_book(self, book):
        if book not in self.__borrowed_books:
            raise ValueError('Book is not borrowed')
        self.__borrowed_books.remove(book)

    @property
    def borrowed_books(self):
        return self.__borrowed_books.copy()  

    @property
    def borrowing_history(self):
        return self.__borrowing_history.copy()  

    def __str__(self):
        return f'{super().__str__()} -> Major: {self.__major}, Year: {self.__year}'
