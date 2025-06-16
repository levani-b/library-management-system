from models.person import Person
from utils.generate_id import generate_id

def main():
    id = generate_id("harry", "poTTeR")
    person = Person("harry", "poTTeR", id, "harry.potterm@gmail.com")

    print(person)
    
    
if __name__ == "__main__":
    main()