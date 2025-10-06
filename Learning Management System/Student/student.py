from Person.person import Person
from Course.courselist import CourseList
# a child class of Person meaning : Inheritance
# Association: means that one class uses another class
# student USE-A courselist to access list of courses
class Student(Person):
    def __init__(self, seat_no ,name, age, email,gender, course_list = None, department = None):
        super().__init__(name, age, email,gender)
        self._seat_no = seat_no
        self._department = department
        # Aggeration : meaning student has a list of courses, and it can exist independently
        if course_list is not None:
            self._course_list = course_list
        else:
            self._course_list = CourseList()
        

    @property
    def seat_no(self):
        return self._seat_no
    @seat_no.setter
    def seat_no(self, seat_no):
        if not isinstance(seat_no, int):
            raise ValueError("Seat number must be an integer")
        if seat_no <= 0:
            raise ValueError("Seat number must be positive")
        self._seat_no = seat_no
    
    @property
    def department(self):
        return self._department
    @department.setter
    def department(self, department):
        if department is not None and not isinstance(department, str):
            raise ValueError("Department must be a string or None")
        if department is not None and not department.strip():
            raise ValueError("Department cannot be an empty string")
        self._department = department.strip() if department else None

    # Course Methods
    def add_course(self, course):
        self._course_list.add_course(course)
    
    def remove_course(self, course_id):
        self._course_list.remove_course(course_id)
    
    def display_courses(self):
        self._course_list.display_courses()
    
    def display_information(self):
        
        print("----- STUDENT INFORMATION -----")
        print(f"Seat No   : {self._seat_no}")
        print(f"Name      : {self._name}")
        print(f"Email     : {self._email}")
        print(f"Age       : {self._age}")
        print(f"Gender    : {self._gender}")
        print(f"Department: {self._department}")
        print("------------------------------")
    
    def __str__(self):
        return f"Seat No: {self._seat_no}, Name: {self._name}"
