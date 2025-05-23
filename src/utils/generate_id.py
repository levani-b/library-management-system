import uuid

def generate_student_id_with_uuid(year):
    uuid_suffix = uuid.uuid4().hex[:8]
    return f'{year}-{uuid_suffix}'