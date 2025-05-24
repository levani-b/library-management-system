from models.person import Person
from models.student import Student
from models.librarian import Librarian
from utils.generate_id import generate_student_id_with_uuid

def main():
    try:
        
        person1 = Person("John", "Doe", "john@email.com", "+1234567890", "P001")
        print("--- PERSON ---")
        print(person1)
        print(f"Full name: {person1.full_name}")

        
        student_id = generate_student_id_with_uuid(2024)
        student1 = Student("Alice", "Smith", "alice@email.com", "+1987654321", 
                          "S001", "Computer Science", 2, student_id)
        
        print("--- STUDENT ---")
        print(f"Student ID: {student1.student_id}")
        print(f"Major: {student1.major}")
        print(f"Year: {student1.year}")
        print(f"Borrowed books: {student1.borrowed_books}")

        student1.add_borrowed_book("Python Programming")
        student1.add_borrowed_book("Data Structures")
        print(f"After borrowing: {student1.borrowed_books}")
        
        student1.add_to_history("Borrowed Python Programming on 2024-01-15")
        print(f"History: {student1.borrowing_history}") 



        librarian1 = Librarian("Bob", "Wilson", "bob@library.com", "+1555123456", 
                              "L001", "regular", "LB1001")
        print(librarian1)
        
        
        librarian2 = Librarian("Sarah", "Johnson", "sarah@library.com", "+1555987654",
                              "L002", "admin", "LB1002")
        print(librarian2)
        
        
        librarian3 = Librarian("Mike", "Davis", "mike@library.com", "+1555456789",
                              "L003", "super_admin", "LB1003")
        print(librarian3)
        
        
        print("\n=== PERMISSION TESTS ===")
        
       
        try:
            librarian1.add_book("New Python Book")
        except PermissionError as e:
            print(f"Regular librarian denied: {e}")
        
        
        try:
            librarian2.add_book("Advanced Algorithms")
        except PermissionError as e:
            print(f"Admin denied: {e}")
        
       
        try:
            librarian3.add_book("Database Design")
        except PermissionError as e:
            print(f"Super admin denied: {e}")
        

        try:
            librarian1.remove_user("S001") 
        except PermissionError as e:
            print(f"Regular librarian can't remove: {e}")
            
        try:
            librarian2.remove_user("S001")  
        except PermissionError as e:
            print(f"Admin can't remove: {e}")
            
        try:
            librarian3.remove_user("S001")  
        except PermissionError as e:
            print(f"Super admin denied: {e}")
        
      
        print("\n=== VALIDATION TESTS ===")
        try:
            bad_librarian = Librarian("Test", "User", "test@test.com", "+1234567890",
                                    "L999", "invalid_level", "LB9999")
        except ValueError as e:
            print(f"Invalid access level caught: {e}")
            
        try:
            bad_employee_id = Librarian("Test", "User", "test@test.com", "+1234567890",
                                      "L999", "regular", "invalid_id")
        except ValueError as e:
            print(f"Invalid employee ID caught: {e}")
    except ValueError as e:
        print(f'Validation Error: {e}')



if __name__ == "__main__":
    main()