def occurance(num):
    num_count={}
    for x in num:
        if x in num_count:
            num_count[x]+=1
        else:
            num_count[x]=1
    print(num_count)

occurance([1,1,1,12,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,445])
