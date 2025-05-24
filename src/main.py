from models import Person, Student, Librarian, Book

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
        
        print("\n=== BOOK TEST ===")
        
        
        book1 = Book("9781234567890", "Python Programming", "John Smith", 
                    "Programming", 2023, 5)
        book2 = Book("978-0-123456-78-9", "Data Structures", "Jane Doe", 
                    "Computer Science", 2022, 3)
        book3 = Book("9780987654321", "Web Development", "Bob Johnson", 
                    "Programming", 2024, 2)
        
        print(book1)
        print(book2)
        print(book3)
        
       
        print(f"\nBook1 available: {book1.is_available()}")
        print(f"Book1 copies: {book1.copies_available}/{book1.total_copies}")
        
       
        print("\n=== BORROWING TEST ===")
        print("Borrowing book1...")
        book1.borrow_copy()
        print(f"After borrowing: {book1.copies_available}/{book1.total_copies}")
        
        print("Borrowing book1 again...")
        book1.borrow_copy()
        print(f"After 2nd borrow: {book1.copies_available}/{book1.total_copies}")
        
      
        print("\n=== RETURNING TEST ===")
        print("Returning book1...")
        book1.return_copy()
        print(f"After return: {book1.copies_available}/{book1.total_copies}")
        

        print("\n=== EDGE CASE TESTS ===")
        
        try:
            for i in range(10): 
                book3.borrow_copy()
                print(f"Borrowed copy {i+1}: {book3.copies_available} left")
        except Exception as e:
            print(f"Borrowing failed: {e}")
        
        
        try:
            for i in range(5):
                book3.return_copy()
                print(f"Returned copy {i+1}: {book3.copies_available} available")
        except Exception as e:
            print(f"Return failed: {e}")
        
        print("\n=== SORTING TEST ===")
        books = [book1, book2, book3]
        books.sort()
        print("Books sorted by title:")
        for book in books:
            print(f"  {book.title}")
        
        
        print("\n=== EQUALITY TEST ===")
        book4 = Book("9781234567890", "Different Title", "Different Author", 
                    "Different Genre", 2020, 1)
        print(f"book1 == book4 (same ISBN): {book1 == book4}")
        print(f"book1 == book2 (different ISBN): {book1 == book2}")
        
        
        print("\n=== VALIDATION TESTS ===")
        
        try:
            bad_isbn = Book("invalid-isbn", "Test", "Test", "Test", 2023, 1)
        except ValueError as e:
            print(f"Invalid ISBN caught: {e}")
        
        try:
            bad_year = Book("9781111111111", "Test", "Test", "Test", -100, 1)
        except ValueError as e:
            print(f"Invalid year caught: {e}")
            
        try:
            empty_title = Book("9782222222222", "", "Test", "Test", 2023, 1)
        except ValueError as e:
            print(f"Empty title caught: {e}")
        
       
        print("\n=== PROPERTY CHANGE TESTS ===")
        print(f"Original book1 title: {book1.title}")
        book1.title = "Advanced Python Programming"
        print(f"New book1 title: {book1.title}")
        
        try:
            book1.copies_available = 10  
        except ValueError as e:
            print(f"Invalid available copies caught: {e}")
            

    except ValueError as e:
        print(f'Validation Error: {e}')




if __name__ == "__main__":
    main()