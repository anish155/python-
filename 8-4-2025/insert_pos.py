def finding_pos():
    nums=[1,3,5,6]
    number=int(input("Enter the number:"))
    nums.append(number)
    nums.sort()

    position=nums.index(number)
    print(f"The number {number} is at position {position} (0-based index) in the sorted list.")


finding_pos()

