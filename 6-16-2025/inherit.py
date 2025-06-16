class id:
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone
    
    def take_data():
        name=input("Enter your name:")
        address=input("Enter your address:")
        phone=int(input("Enter your phone number:"))
        return name,address,phone
    
    def display_id(self):
        print("Displaying common info:")
        print("Name:",self.name)
        print("Address:",self.address)
        print("Phone:",self.phone)

class student(id):
    def __init__(self,name,address,phone,roll_no,section,fee):
        super().__init__(name,address,phone)
        self.roll_no=roll_no
        self.section=section
        self.fee=fee

    def student_data():
        roll_no=int(input("Enter the Roll no:"))
        section=int(input("Enter the Section:"))
        fee=int(input("Enter the Fee:"))
        return roll_no,section,fee
    
    def stud_display(self):
        super().display_id()
        print("Students ID")
        print("Roll no:",self.roll_no)
        print("Section:",self.section)
        print("Fee:",self.fee)

class teacher(id):
    def __init__(self,name,address,phone,subject,salary):
        super().__init__(name,address,phone)
        self.subject=subject
        self.salary=salary

    def teacher_data():
        subject=input("Enter the Subject;")
        salary=int(input("Enter the Salary:"))
        return subject,salary

    def teach_display(self):
        super().display_id()
        print("Teachers ID")
        print("Subject:",self.subject)
        print("Salary:",self.salary)

while(True):
    choice=int(input("enter your choice (1 or 2):"))
    if(choice==1):
        name,address,phone=id.take_data()
        roll_no,section,fee=student.student_data()
        stud = student(name, address, phone, roll_no, section, fee)
        stud.stud_display()
    elif(choice==2):
        name,address,phone=id.take_data()
        subject,salary=teacher.teacher_data()
        teach=teacher(name,address,phone,subject,salary)
        teach.teach_display()
    else:
        break

    cont=input("do you want to continue ('y' or 'n'):")
    if cont.lower()!='y':
        print("Exiting...")
        break
