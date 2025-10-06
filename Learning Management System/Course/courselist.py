from Course.course import Course
from range import Range

# Aggeration: CourseList HAS-A Course objects, but they can exist INDEPENDENTLY (not owned by anyone)
class CourseList:
    def __init__(self, size=3):
        self._courses: list[Course | None] = [None] * size
        # initially filled with none values to indicate empty slots
        self._count = 0
        self._size = size

    def _increase_size(self):
        """Double the list size when full."""
        new_size = self._size * 2
        # doubles capacity when full
        new_list: list[Course | None] = [None] * new_size
        for i in Range(self._count):
            new_list[i] = self._courses[i]
            #copy old elements to new list
        self._courses = new_list
        # update reference to new list
        self._size = new_size
        # update size

    def add_course(self, course):
        """Add a course to the list."""
        if not isinstance(course, Course):
            raise TypeError("Only Course objects can be added.")

        if self._count >= self._size:
            self._increase_size()

        self._courses[self._count] = course
        self._count += 1
        print(f"Course {course.course_name} added successfully.")

    def remove_course(self, course_id):
        """Remove a course by ID."""
        for i in Range(self._count):
            if self._courses[i] and self._courses[i].course_id == course_id:
                for j in Range(i, self._count - 1):
                    self._courses[j] = self._courses[j + 1]
                self._courses[self._count - 1] = None
                self._count -= 1
                print(f"Course {course_id} removed successfully.")
                return
        print(f"Course {course_id} not found.")

    def search_by_id(self, course_id):
        """Find index of course by ID."""
        for i in Range(self._count):
            if self._courses[i] and self._courses[i].course_id == course_id:
                return i
        return -1

    def display_courses(self):
        """Display all courses."""
        if self._count == 0:
            print("No courses available.")
            return

        print("\n--- Course List ---")
        for i in Range(self._count):
            print(self._courses[i])

    def status(self):
        """Show how many courses exist and available space."""
        remaining = self._size - self._count
        print(f"Total Courses: {self._count} | Capacity: {self._size} | Remaining: {remaining}")
