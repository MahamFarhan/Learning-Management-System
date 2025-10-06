from Person.person import Person

# a child class of Person meaning : Inheritance
class Teacher(Person):
    def __init__(self, subject, name, age,gender,email):
        super().__init__(name, age,email,gender)
        self._subject = subject
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self, subject):
        if not isinstance(subject, str):
            raise ValueError("Subject must be a string")
        if not subject.strip():
            raise ValueError("Subject cannot be empty")
        self._subject = subject.strip()
    
    def display_teacher_info(self):
        print("----- TEACHER INFORMATION -----")
        print(f"Subject : {self._subject}")
        print(f"Name    : {self._name}")
        print(f"Email   : {self._email}")
        print(f"Age     : {self._age}")
        print(f"Gender  : {self._gender}")
        print(f"Subject : {self._subject}")
        print("------------------------------")
    def __str__(self):
        return f"Name: {self._name}, Subject: {self._subject}, Email: {self._email}, Age: {self._age}"
