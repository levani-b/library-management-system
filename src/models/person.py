import re

class Person:
    def __init__(self, first_name, last_name, email, phone, person_id):
        self.__first_name = first_name        
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__person_id = person_id
    
    # --- First Name ---
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__first_name = value
        
    # --- Last Name ---
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty")
        self.__last_name = value
    
    # --- Full Name ---
    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'
    
    # --- Email ---
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not re.match(r"^\+?[\d\s\-\(\)]{7,15}$", value.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")):
            raise ValueError("Invalid email format")
        self.__email = value
    
    # --- Phone ---
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        if not re.match(r"^\+?\d{7,15}$", value):
            raise ValueError("Invalid phone number. Must be 7–15 digits, optionally starting with +.")
        self.__phone = value
    
    # --- Person ID ---
    @property
    def person_id(self):
        return self.__person_id
    
    @person_id.setter
    def person_id(self, value):
        if not value.strip():
            raise ValueError("Person ID can not be empty")
        self.__person_id = value
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.person_id == other.person_id
        return False

    def __str__(self):
        return f"Person(First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email}, Phone: {self.__phone}, Person ID: {self.__person_id})"