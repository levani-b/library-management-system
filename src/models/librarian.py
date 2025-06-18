from enum import Enum
from models.person import Person

class AccessLevel(Enum):
   REGULAR = 'regular'
   ADMIN = 'admin'
   SUPER_ADMIN = 'super_admin'

class Librarian(Person):
   PERMISSIONS = {
       'manage_books': ['admin', 'super_admin'],
       'manage_students': ['admin', 'super_admin'],
       'manage_librarians': ['super_admin'],
       'generate_reports': ['admin', 'super_admin'],
       'process_transactions': ['regular', 'admin', 'super_admin'],
       'search_books': ['regular', 'admin', 'super_admin'],
       'view_student_info': ['regular', 'admin', 'super_admin']
   }

   def __init__(self, name, surname, id, email, access_level):
       super().__init__(name, surname, id, email)
       self.__access_level = self.__validate_access_level(access_level)

   def __validate_access_level(self, value):
       if isinstance(value, AccessLevel):
           return value.value
       if not isinstance(value, str):
           raise TypeError('Access level must be string')
       valid_levels = [level.value for level in AccessLevel]
       if value not in valid_levels:
           raise ValueError(f'Access level must be one of: {", ".join(valid_levels)}')
       return value

   @property
   def access_level(self):
       return self.__access_level

   @access_level.setter
   def access_level(self, value):
       self.__access_level = self.__validate_access_level(value)

   def has_permission(self, action):
       if action not in self.PERMISSIONS:
           raise ValueError(f'Unknown action: {action}')
       return self.__access_level in self.PERMISSIONS[action]

   def is_admin(self):
       return self.__access_level in ['admin', 'super_admin']

   def is_super_admin(self):
       return self.__access_level == 'super_admin'

   def is_regular(self):
       return self.__access_level == 'regular'

   def __str__(self):
       return f'{super().__str__()} -> Access Level: {self.__access_level}'