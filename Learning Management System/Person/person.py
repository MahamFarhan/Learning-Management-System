class Person:
    # a Parent class for Student and Teacher
    def __init__(self, name, age, email, gender):
        self._name = name
        self._age = age
        self._email = email
        self._gender = gender
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name 
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self._name = name.strip()

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        self._email = email.strip()

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if gender.lower() not in ['male', 'female', 'other']:
            raise ValueError("Gender must be 'male', 'female', or 'other'")
        self._gender = gender.lower()
    
    def display_information(self):
         """Prints all basic info in a neat format."""
         print("----- PERSON INFORMATION -----")
         print(f"Name   : {self._name}")
         print(f"Email  : {self._email}")
         print(f"Age    : {self._age}")
         print(f"Gender : {self._gender}")
         print("------------------------")

    def __str__(self):
        return f"Name: {self._name}, Email: {self._email}, Age: {self._age}, Gender: {self._gender}"