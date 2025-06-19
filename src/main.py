from models.library import Library
from gui.main_window import LibraryMainWindow
from models.book import Book
from models.student import Student
from models.librarian import Librarian, AccessLevel
from utils.generate_id import generate_id

def add_example_data(library):
    if not library.books:
        books = [
            Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532699", "Fantasy", 1997, 3, 3),
            Book("The Hobbit", "J.R.R. Tolkien", "9780261102217", "Fantasy", 1937, 2, 2),
            Book("1984", "George Orwell", "9780451524935", "Dystopian", 1949, 4, 4),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic", 1960, 5, 5),
            Book("Pride and Prejudice", "Jane Austen", "9780141439518", "Romance", 1813, 2, 2),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic", 1925, 3, 3),
            Book("A Brief History of Time", "Stephen Hawking", "9780553380163", "Science", 1988, 2, 2),
            Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", "Classic", 1951, 3, 3),
            Book("The Da Vinci Code", "Dan Brown", "9780307474278", "Thriller", 2003, 4, 4),
            Book("The Alchemist", "Paulo Coelho", "9780061122415", "Adventure", 1988, 2, 2),
            Book("The Road", "Cormac McCarthy", "9780307387899", "Post-apocalyptic", 2006, 2, 2),
            Book("The Girl with the Dragon Tattoo", "Stieg Larsson", "9780307454546", "Mystery", 2005, 3, 3),
            Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "9780062316097", "History", 2011, 2, 2),
            Book("The Shining", "Stephen King", "9780307743657", "Horror", 1977, 2, 2),
            Book("Moby Dick", "Herman Melville", "9781503280786", "Classic", 1851, 1, 1),
        ]
        for book in books:
            library.add_book(book)
    if not library.students:
        students = [
            Student("Alice", "Smith", generate_id("Alice", "Smith"), "alice.smith@example.com", "Literature", 1),
            Student("Bob", "Johnson", generate_id("Bob", "Johnson"), "bob.johnson@example.com", "Physics", 2),
            Student("Charlie", "Williams", generate_id("Charlie", "Williams"), "charlie.williams@example.com", "Mathematics", 3),
            Student("Diana", "Brown", generate_id("Diana", "Brown"), "diana.brown@example.com", "Biology", 4),
            Student("Ethan", "Jones", generate_id("Ethan", "Jones"), "ethan.jones@example.com", "Engineering", 2),
            Student("Fiona", "Garcia", generate_id("Fiona", "Garcia"), "fiona.garcia@example.com", "History", 1),
            Student("George", "Martinez", generate_id("George", "Martinez"), "george.martinez@example.com", "Computer Science", 3),
            Student("Hannah", "Rodriguez", generate_id("Hannah", "Rodriguez"), "hannah.rodriguez@example.com", "Chemistry", 4),
            Student("Ivan", "Lee", generate_id("Ivan", "Lee"), "ivan.lee@example.com", "Economics", 2),
            Student("Julia", "Walker", generate_id("Julia", "Walker"), "julia.walker@example.com", "Philosophy", 1),
        ]
        for student in students:
            library.register_student(student)
    if not library.librarians:
        librarians = [
            Librarian("Clara", "Brown", generate_id("Clara", "Brown"), "clara.brown@example.com", AccessLevel.ADMIN.value),
            Librarian("David", "Wilson", generate_id("David", "Wilson"), "david.wilson@example.com", AccessLevel.REGULAR.value),
            Librarian("Emily", "Moore", generate_id("Emily", "Moore"), "emily.moore@example.com", AccessLevel.SUPER_ADMIN.value),
            Librarian("Frank", "Taylor", generate_id("Frank", "Taylor"), "frank.taylor@example.com", AccessLevel.ADMIN.value),
        ]
        for librarian in librarians:
            library.register_librarian(librarian)

def main():
    library = Library("Central Library")
    add_example_data(library)
    app = LibraryMainWindow(library)
    app.mainloop()

if __name__ == "__main__":
    main()