from Student.studentlist import StudentList
from Course.courselist import CourseList
from Course.course import Course
from Student.student import Student
class Admin:
    # Association: Admin USES-A StudentList and CourseList
    # Composition: Admin HAS-A StudentList and CourseList
    # when the admin object is destroyed, the student list and course list are also destroyed
    def __init__(self):
        self.students = StudentList()
        self.courses = CourseList(6)
    
    def setup_courses(self):
       self.courses.add_course(Course("Fundamentals of Object Oriented Programming", 4, "CS101"))
       self.courses.add_course(Course("Digital Logic Design", 3, "CS105"))
       self.courses.add_course(Course("Discrete Structures", 2, "CS198"))
       self.courses.add_course(Course("Communication and Presentation", 1, "CS001"))
       self.courses.add_course(Course("Pakistan Studies", 1, "CS102"))
       self.courses.add_course(Course("Linear Algebra", 2, "CS160"))
    
    def run(self):
        print("\n=== All Available Courses in DCS ===")
        self.courses.display_courses()

        print("\n---- Admitting Students ----")
        self.students.add_student(Student(123, "Ali", 20, "ali@gmail.com","male", self.courses, "Computer Science"))
        self.students.add_student(Student(234, "Aisha", 18, "aisha@gmail.com", "female", self.courses, "Computer Science"))
        self.students.add_student(Student(345, "Ahmed", 19, "ahmed@gmail.com", "male", self.courses, "Computer Science"))

        print("\n---- All Admitted Students ----")
        self.students.display_students()

        # Add new student mid-semester
        s_new = Student(456, "Sara", 20 , "sara@mail.com", "female", self.courses, "Software Engineering")
        self.students.add_student(s_new)

        print("\n---- Searching by seat number ----")
        index = self.students.search_by_seat(234)
        if index != -1:
            print("Student Details:")
            student = self.students.get_student(index) 
        if student is not None:
            student.display_information()
        #remove a student
        
        print("\n---- Removing a student ----")
        self.students.remove_student(345)
        
        print("\n---- All Remaining Students ----")
        self.students.display_students()

        print("\n---- Student List Status ----")
        self.students.status()
