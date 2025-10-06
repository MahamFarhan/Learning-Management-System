class Course:
    def __init__(self, course_name, credit_hour, course_id):
        self._course_name = course_name
        self._credit_hour = credit_hour
        self._course_id = course_id

    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, course_name):
        if not isinstance(course_name, str):
            raise ValueError("Course name must be a string")
        if not course_name.strip():
            raise ValueError("Course name cannot be empty")
        self._course_name = course_name.strip()

    @property
    def credit_hour(self):
        return self._credit_hour
    @credit_hour.setter
    def credit_hour(self, credit_hour):
        if not isinstance(credit_hour, int):
            raise ValueError("Credit hour must be an integer")
        if credit_hour <= 0:
            raise ValueError("Credit hour must be a positive integer")
        self._credit_hour = credit_hour
    
    @property
    def course_id(self):
        return self._course_id
    @course_id.setter
    def course_id(self, course_id):
        if not isinstance(course_id, str):
            raise ValueError("Course ID must be a string")
        if not course_id.strip():
            raise ValueError("Course ID cannot be empty")
        self._course_id = course_id.strip()
    
    def display_info(self):
        print("----- COURSE INFORMATION -----")
        print(f"Course Name : {self._course_name}")
        print(f"Course ID   : {self._course_id}")
        print(f"Credit Hour : {self._credit_hour}")
        print("------------------------------")
    
    def __str__(self):
        return f"Course Name: {self._course_name}, Course ID: {self._course_id}, Credit Hour: {self._credit_hour}"
    