class Student:
    def __init__(self, student, age=13, grade="12th"):
        self._student = student
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._student
   
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) >= 3 and new_name.istitle():
                self._student = new_name
            else:
                print("Name must contain only letters and be longer than two letters")
        else:
            print("Invalid input for student. Must be a string.")
   
    @property
    def get_age(self):
        return self._age
   
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print("Invalid input for age. Must be an integer between 12 and 17.")
   
    @property
    def get_grade(self):
        return self._grade
   
    @get_grade.setter
    def set_grade(self, new_grade):
        valid_grades = ["9th", "10th", "11th", "12th"]
        if new_grade.endswith('th') and new_grade in valid_grades:
            self._grade = new_grade
        else:
            print("Invalid input for grade. Must be formatted as '9th', '10th', '11th', or '12th'.")
   
    def __str__(self):
        return f"Student student: {self._student}, Age: {self._age}, Grade: {self._grade}"
   
    def advance(self, years_advanced=1):
        new_grade_number = int(self._grade[:-2]) + years_advanced
        new_grade = f"{new_grade_number}th"
        self._grade = new_grade  # Update the grade attribute
        print(f"{self.student} has advanced to the {new_grade} grade.")
   
    def study(self, subject):
        print(f"{self.student} is studying {subject}.")
