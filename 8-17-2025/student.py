class Student:
    def __init__(self):
        self.name = None
        self.roll = 0
        
    def info(self):
        self.name = input("Enter the name: ")
        self.roll = int(input("Enter the roll no: "))

class Marks(Student):
    def __init__(self):
        super().__init__()
        self.marks = []   

    def subjects(self):
        subjects = ["Math", "Science", "English"]
        for sub in subjects:
            mark = int(input(f"Enter {sub} marks: "))
            self.marks.append(mark)

    def result(self):
        
        if all(mark >= 40 for mark in self.marks):
            print(f"{self.name} (Roll {self.roll}) has PASSED ✅")
        else:
            print(f"{self.name} (Roll {self.roll}) has FAILED ❌")


s1 = Marks()
s1.info()
s1.subjects()
print("Marks:", s1.marks)
s1.result()
