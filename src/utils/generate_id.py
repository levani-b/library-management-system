import uuid

def generate_id(name, surname):
    unique = str(uuid.uuid4())
    unique_id = f'{name[0].upper()}_{surname[0].upper()}_{unique}'
    return unique_id