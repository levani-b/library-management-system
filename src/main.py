from models.person import Person
from models.student import Student

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

if __name__ == "__main__":
    main()