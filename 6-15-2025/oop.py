class Person:
    race = "mongolian"
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Race: {Person.race}"

    @staticmethod
    def Pname():
        name = input("Enter your name: ")
        return name

    @staticmethod
    def Paddress():
        address = input("Enter your address: ")
        return address

# Create a Person instance after the class is fully defined
Pername = Person.Pname()
Peraddress = Person.Paddress()
P1 = Person(Pername, Peraddress)
print(P1)