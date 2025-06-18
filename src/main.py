from models.person import Person
from models.student import Student
from models.librarian import Librarian, AccessLevel
from utils.generate_id import generate_id

def main():
    person1 = Person("john", "doe", generate_id("john", "doe"), "john.doe@gmail.com")
    person2 = Person("jane", "smith", generate_id("jane", "smith"), "jane.smith@yahoo.com")
    
    print(person1)
    print(person2)
    print(person1 == person2)
    
    student1 = Student("harry", "potter", generate_id("harry", "potter"), 
                      "harry.potter@hogwarts.edu", "Magic", 3)
    student2 = Student("hermione", "granger", generate_id("hermione", "granger"), 
                      "hermione.granger@hogwarts.edu", "Magic", 3)
    
    print(student1)
    print(student2)
    print(student1.major)
    print(student2.year)
    
    student1.year = 4
    student2.major = "Advanced Magic"
    
    print(student1)
    print(student2)

    librarian1 = Librarian("minerva", "mcgonagall", generate_id("minerva", "mcgonagall"),
                          "minerva.mcgonagall@hogwarts.edu", AccessLevel.SUPER_ADMIN.value)
    librarian2 = Librarian("madam", "pince", generate_id("madam", "pince"),
                          "madam.pince@hogwarts.edu", AccessLevel.REGULAR.value)
    
    print("\nLibrarian Information:")
    print(librarian1)
    print(librarian2)
    
    print("\nPermission Checks:")
    print(f"Can {librarian1.name} manage librarians? {librarian1.has_permission('manage_librarians')}")
    print(f"Can {librarian2.name} manage librarians? {librarian2.has_permission('manage_librarians')}")
    
    print("\nChanging Madam Pince's access level to admin:")
    librarian2.access_level = AccessLevel.ADMIN.value
    print(f"Can {librarian2.name} manage books? {librarian2.has_permission('manage_books')}")
    print(f"Can {librarian2.name} manage students? {librarian2.has_permission('manage_students')}")
    print(f"Can {librarian2.name} manage librarians? {librarian2.has_permission('manage_librarians')}")
    print(f"Can {librarian2.name} process transactions? {librarian2.has_permission('process_transactions')}")
    
    print("\nAccess Level Checks:")
    print(f"Is {librarian1.name} regular? {librarian1.is_regular()}")
    print(f"Is {librarian1.name} admin? {librarian1.is_admin()}")
    print(f"Is {librarian1.name} super admin? {librarian1.is_super_admin()}")
    
    print(f"\nIs {librarian2.name} regular? {librarian2.is_regular()}")
    print(f"Is {librarian2.name} admin? {librarian2.is_admin()}")
    print(f"Is {librarian2.name} super admin? {librarian2.is_super_admin()}")
    
    print("\nTrying to set invalid access level:")
    try:
        librarian2.access_level = "invalid_level"
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTrying to check invalid permission:")
    try:
        librarian1.has_permission("invalid_action")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()