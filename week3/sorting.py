def bubble(num):
    for i in range(len(num)):
        for j in range(0,len(num)-i-1):
            if(num[j]>num[j+1]):
                num[j],num[j+1]=num[j+1],num[j]
                print(num)


num=[6,3,8,1,0,5,9,2]
bubble(num)
