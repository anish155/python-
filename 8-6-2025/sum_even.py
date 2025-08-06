def even():
    sum_even=0
    for num in range(1,101):
        if num%2==0:
            sum_even+=num
    return sum_even
    
print(even())