from models.person import Person
from models.student import Student
from utils.generate_id import generate_student_id_with_uuid

def main():
    try:
        # Person
        person1 = Person("John", "Doe", "john@email.com", "+1234567890", "P001")
        print("--- PERSON ---")
        print(person1)
        print(f"Full name: {person1.full_name}")

        # Student
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
    except ValueError as e:
        print(f'Validation Error: {e}')



if __name__ == "__main__":
    main()