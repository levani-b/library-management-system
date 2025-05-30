import uuid
from datetime import datetime

def generate_person_id(role='P'):
    """
    Generate a unique ID for a person with format: [role][year][uuid]
    role: 'S' for student, 'L' for librarian, 'P' for generic person
    """
    current_year = datetime.now().year
    uuid_suffix = uuid.uuid4().hex[:6]
    return f'{role}{current_year}{uuid_suffix}'

def generate_student_id():
    return generate_person_id('S')

def generate_librarian_id():
    return generate_person_id('L')