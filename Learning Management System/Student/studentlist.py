from Student.student import Student
from range import Range

class StudentList:
    # Aggeration: StudentList contains Student objects, but they can exist independently
    def __init__(self, size=3):
        self._students: list[Student | None] = [None] * size
        self._count = 0
        self._size = size

    def _increase_size(self):
        """Doubles the size of the list when full."""
        new_size = self._size * 2
        new_students: list[Student | None] = [None] * new_size
        for i in Range(self._count):
            new_students [i] = self._students[i]
        self._students = new_students
        self._size = new_size

    def add_student(self, student):
        """Add a new student at the end of the list."""
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")

        # Prevent duplicate seat numbers
        if self.search_by_seat(student.seat_no) != -1:
            raise ValueError(f"Student with seat number {student.seat_no} already exists.")

        if self._count >= self._size:
            self._increase_size()

        self._students[self._count] = student
        self._count += 1
        print(f"Student {student.name} added successfully.")

    def add_student_at(self, student, index):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")
        #Insert a student at a specific index.
        # if index is out of bounds, raise IndexError
        if index < 0 or index > self._count:
            raise IndexError("Invalid index.")
        # if count is equal to size, increase size
        if self._count >= self._size:
            self._increase_size()

        for i in Range(self._count, index, -1):
            # shift elements to the right
            self._students[i] = self._students[i - 1]
            # add the new student at the specified index

        self._students[index] = student
        self._count += 1
        print(f"Student {student.name} added at index {index}.")

    def search_by_seat(self, seat_no):
        """Search for a student by seat number and return index."""
        for i in Range(self._count):
            if self._students[i] and self._students[i].seat_no == seat_no:
                return i
        return -1

    def update_student(self, seat_no, updated_student):
        """Replace an existing student record with new details."""
        index = self.search_by_seat(seat_no)
        if index == -1:
            print("No student found with that seat number.")
            return
        self._students[index] = updated_student
        print(f"Student with seat number {seat_no} updated successfully.")

    def remove_student(self, seat_no):
        """Remove student record by seat number."""
        index = self.search_by_seat(seat_no)
        if index == -1:
            print("No student found.")
            return

        for i in Range(index, self._count - 1):
            self._students[i] = self._students[i + 1]

        self._students[self._count - 1] = None
        self._count -= 1
        print(f"Student with seat number {seat_no} removed successfully.")

    def get_student(self, index):
        if 0 <= index < self._count:
         return self._students[index]
        raise IndexError("Index out of bounds.")
    # a getter method to retrieve student at a specific index because accessing a private 
    # attribute directly from outside the class is not a good practice
    
      
    def display_students(self):
        """Display all students."""
        if self._count == 0:
            print("No students in the list.")
            return

        print("\n--- Student List ---")
        for i in Range(self._count):
            print(self._students[i])

    def status(self):
        """Show list capacity and remaining space."""
        remaining = self._size - self._count
        print(f"Total Students: {self._count} | Capacity: {self._size} | Remaining: {remaining}")
