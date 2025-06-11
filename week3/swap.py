def take():
    naam=input("enter your name:")
    umer=int(input("Enter your age:"))
    return naam,umer

def dictionary(naam,umer):
    person={"name":naam,
            "age":umer}
    return person

def swap(person):
    person["name"],person["age"]=person["age"],person["name"]

naam,umer=take()
person=dictionary(naam,umer)
swap(person)
print(person)