class student():

    def __init__(self,name,roll,grade):
        self.__name=name
        self.__rollno=roll
        self.__grade=grade

    def name_input():
        name=input("Enter student name:")
        return name
    
    def roll_input():
        roll=int(input("Enter student roll no:"))
        return roll
    
    def grade_input():
        grade=int(input("Enter student grade:"))
        return grade
    
    def get_name(self):
        return self.__name

    def get_rollno(self):
        return self.__rollno

    def get_grade(self):
        return self.__grade
    
    def set_name(self, name):
        self.__name = name

    def set_rollno(self, roll):
        self.__rollno = roll

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Must be between 0 and 100.")

name = student.name_input()
roll = student.roll_input()
grade = student.grade_input()

s1 = student(name, roll, grade)

print("Student Info:")
print("Name:", s1.get_name())
print("Roll No:", s1.get_rollno())
print("Grade:", s1.get_grade())

s1.set_grade(95)
print("Updated Grade:", s1.get_grade())