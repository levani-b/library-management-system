from models import Person

def main():
    try:
        person1 = Person("John", "Doe", "john@email.com", "+1234567890", "P001")
        print(person1)
        print(f"Full name: {person1.full_name}")

        person1.email = 'invalid-email'
    
    except ValueError as e:
        print(f'Validation Error: {e}')



if __name__ == "__main__":
    main()