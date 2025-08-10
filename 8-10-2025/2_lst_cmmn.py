def take_lst():
    lst1=[]
    lst2=[]

    print("Enter numbers for first list:")
    for _ in range(4):
        nums1=int(input("Enter the number:"))
        lst1.append(nums1)

    print("Enter numbers for second list:")
    for _ in range(4):
        nums2 = int(input("Enter the number: "))
        lst2.append(nums2)
    
    return lst1,lst2

def common(l1,l2):
    common_lst=[]
    for n1 in l1 :
        if n1 in l2 and n1 not in common_lst:
            common_lst.append(n1)
    return common_lst

l1,l2=take_lst()
print(common(l1,l2))