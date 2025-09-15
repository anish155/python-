def Take():
    array=[]
    print("INSERTING DATA")
    for i in range(5):
        element=int(input("Enter the numbers:"))
        array.append(element)
    return array

def left_rotation(nums, rotation):
    rotation=rotation%len(nums)
    return nums[rotation:]+nums[:rotation]

def right_rotation(nums, rotation): 
    rotation=rotation%len(nums)
    return nums[-rotation:]+nums[:-rotation]

nums=Take()
rotation = int(input("Enter the amount for rotation to occur: "))

print("Left rotation:", left_rotation(nums, rotation))
print("Right rotation:", right_rotation(nums, rotation))