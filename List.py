number=[1,2,3,4,5,6,7,8,9,0]
sum=13
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i]+number[j]==sum:
            print(f"index:{i},{j}")