def right():
    rows=5
    for i in range(rows+1):
        for j in range(i+1):
            print(j,end=" ")
        print()
    
right()