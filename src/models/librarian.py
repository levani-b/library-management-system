import re
from .person import Person

class Librarian(Person):
    VALID_ACCESS_LEVELS = {"regular", 'admin', 'super_admin'}

    def __init__(self, first_name, last_name, email, phone, person_id, access_level, employee_id):
        super().__init__(first_name, last_name, email, phone, person_id)
        self.__access_level = access_level
        self.__employee_id = employee_id
    
    # --- Access Level ---
    @property
    def access_level(self):
        return self.__access_level

    @access_level.setter
    def access_level(self, value):
        if value not in self.VALID_ACCESS_LEVELS:
            raise ValueError(f"Access level must be one of: {', '.join(self.VALID_ACCESS_LEVELS)}.")
        self.__access_level = value

     # --- Employee ID ---
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not re.match(r"^[A-Z]{2}\d{4}$", value):  # Example: "LB1234"
            raise ValueError("Employee ID must be in format: 2 uppercase letters followed by 4 digits (e.g., LB1234).")
        self.__employee_id = value
    

    # --- Admin Functions ---
    def add_book(self, book):
        if self.__access_level in {"admin", 'super_admin'}:
            print(f"{self.full_name} added book: {book}")
        else:
            raise PermissionError("Insufficient access level to add books.")
    
    def remove_user(self, user_id):
        if self.access_level == "super_admin":
            print(f"{self.full_name} removed user ID: {user_id}")
        else:
            raise PermissionError("Only super_admin can remove users.")
    
    def remove_student(self, student_id):
        if self.access_level in {"admin", "super_admin"}:
            print(f"{self.full_name} removed student ID: {student_id}")
        else:
            raise PermissionError("Insufficient access level to remove students.")

    def remove_librarian(self, employee_id):
        if self.access_level == "super_admin":
            print(f"{self.full_name} removed librarian ID: {employee_id}")
        else:
            raise PermissionError("Only super_admin can remove librarians.")
    
    def __str__(self):
        return (
            f"Librarian(Name: {self.full_name}, "
            f"Employee ID: {self.employee_id}, "
            f"Access Level: {self.access_level}, "
            f"Email: {self.email})"
        )