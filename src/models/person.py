import re

class Person:
    def __init__(self, name, surname, id, email):
        self.__name = self.__validate_name(name)
        self.__surname = self.__validate_surname(surname)
        self.__id = self.__validate_id(id)
        self.__email = self.__validate_email(email)

    def __validate_name(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Name must be string')
        if value == '':
            raise ValueError('Name can not be empty')
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return value.title()

    def __validate_surname(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Surname must be string')
        if value == '':
            raise ValueError('Surname can not be empty')
        if len(value) < 2:
            raise ValueError("Surname must be at least 2 characters long")
        return value.title()

    def __validate_id(self, value):
        if not isinstance(value, str):
            raise TypeError('ID must be string')
        if value == '':
            raise ValueError('ID can not be empty')
        return value

    def __validate_email(self, value):
        value = value.strip().lower()
        if not isinstance(value, str):
            raise TypeError('Email must be string')
        if value == '':
            raise ValueError('Email can not be empty')
        if not self.__is_valid_email(value):
            raise ValueError('Invalid Email format')
        return value
        
    def __is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = self.__validate_name(value)
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, value):
        self.__surname = self.__validate_surname(value)
    
    @property
    def person_id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = self.__validate_email(value)
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.__id == other.__id
    
    def __str__(self):
        return f'{self.__name} {self.__surname} -> ID: {self.__id}, Email: {self.__email}'
    
    