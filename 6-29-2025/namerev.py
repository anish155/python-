def name():
    name=input("Enter your name:")
    return name

def reverse(name):
    reverse=name[::-1]
    print(reverse)

naam=name()
reverse(naam)