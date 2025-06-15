def pyramid(num):
    for point in range(1,num+1):
        for side  in range(num-point):
            print(" ",end="")
        for space in range(2*point-1):
            print("*",end="")
        print("")
pyramid(6)