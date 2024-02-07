# class Student:
#     #Declare properties of Students, to include: Name, Age, grade,
#     #along with a get_name and set_name "getter" that returns the students name or changes it
#     def __init__(self, name, age = 13, grade = "12th"):
#         self._name = name
#         self._age = age
#         self._grade = grade
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         if isinstance(new_name, str):
#             if len(new_name) >= 3 and new_name.istitle():
#                 self._name = new_name
#         else:
#             print("Name must be contain only letters and be longer than two letters")


#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, new_age):
#         if isinstance(new_age, int) and 11 < new_age < 18:
#             self._age = new_age

    
#     @property
#     def grade(self):
#         return self._grade
    
#     @grade.setter
#     def grade(self, new_grade):
#         valid_grades = ["9th", "10th", "11th", "12th"]
#         if new_grade.endswith('th') and new_grade in valid_grades:
#             self._grade = new_grade 

    
#     def __str__(self):
#         return f"Student name: {self._name}, Age: {self._age}, Grade: {self._grade}"
        
#     def advance(self, years_advanced=1):
#         new_grade_number = int(self._grade[:-2]) + years_advanced
#         new_grade = f"{new_grade_number}th"
#         print(f"{self.name} has advanced to the {new_grade}th grade. Nerd")

#     def study(self, subject):
#         print(f"{self.name} is studying {subject}.")

# # Create a student
# student1 = Student("Francisco", age=15, grade="12th")

# # Print initial information
# print(student1)

# # Use setter methods
# student1.name = "Frank"
# student1 = Student("Francisco", age=15, grade="12th")
# print(student1)

# student1.name("Frank")
# student1.age(16)
# student1.grade("11th")
# print(student1)

# student1.advance(1)
# student1.study("Computer Science")

# student1.age = 16
# student1.grade = "11th"

# # Print updated information
# print(student1)

# # Test advance and study methods
# student1.advance(1)
# student1.study("Computer Science")

# # get_age that returns student age and set_age that will update the student's age if they are between the ages of 11 and 18


    
# #get_grade returns student grade and set_grade Required Updates a #students grade only if the grade falls within
# # 9th - 12th grade and the value is formatted with "th"
# # next to the numbered grade


# #methods should look like __str__ which should return the properties of Student

# #OPTIONAL method `advance` will advance the student to the next grade. Nerd

# #Study method shows the major of the student
    
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
        print(f"{self.student} has advanced to the {new_grade} grade. Nerd")
   
    def study(self, subject):
        print(f"{self.student} is studying {subject}.")
# Create a student
# student1 = Student("Francisco", age=15, grade="12th")
# # Print initial information
# print(student1)
# # Use setter methods
# student1.name = "Frank"
# student1.age = 16
# student1.grade = "11th"
# # Print updated information
# print(student1)
# # Test advance and study methods
# student1.advance(1)
# student1.study("Computer Science")