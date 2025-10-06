**Overview:**
A simple **Object-Oriented Python application** that manages students, teachers, and courses efficiently.  
This project demonstrates concepts like **encapsulation, composition, dynamic arrays, and class relationships** in a clean, modular structure.

**Features:**
 - Manage **students** with details like name, age, email, and department  
 - Manage **courses** with course ID, name, and credit hour  
 - Admin panel to **add, remove, and display** students and courses  
 - Custom-built **Range** class (used instead of Python's built-in `range`)  
 - Dynamic **CourseList** and **StudentList** using manual resizing logic  
 - Follows strong **OOP principles** and clean separation of classes

**Class Structure:**
 - `Person` → Base class for Student and Teacher  
 - `Student` → Inherits from Person, includes department and course info  
 - `Teacher` → Inherits from Person, manages assigned courses  
 - `Course` → Represents course details  
 - `CourseList` / `StudentList` → Custom list management classes  
 - `Admin` → Handles setup, operations, and overall management

**Relationship Type:**
 - **Admin** *uses* `CourseList` and `StudentList`
 - **StudentList** *contains* multiple `Student` objects  
 - **CourseList** *contains* multiple `Course` objects  
 - **Student** *has* a list of `Course` objects (composition)
