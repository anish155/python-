def in_list():
    lst=[]
    print("Enter 10 numbers:")
    for i in range(10):
        number=int(input(f"Enter the numbers {i+1}:"))
        lst.append(number)
    
    print("List of numbers:",lst)
    return lst

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))


num=in_list()
duplicates=find_duplicates(num)
print("the duplicate numbers are:",duplicates)

