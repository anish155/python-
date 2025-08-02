def take_nums():
    numbers=[]
    for _ in range(10):
        nums=int(input("Enter the numbers:"))
        numbers.append(nums)
    return numbers

def mode(nums):
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
    
    max_freq=max(freq.values())
    modes= [num for num, count in freq.items() if count == max_freq]
    if len(modes) == len(freq):
        return "No mode found"
    else:
        return modes
    
numbers = take_nums()
print("Mode(s):", mode(numbers))