def numbers():
    lst=[]
    for i in range(10):
        num=int(input("Enter the number:"))
        lst.append(num)
    return lst

def lifo(num):
    while num:
        print(num.pop())

num=numbers()
lifo(num)

        