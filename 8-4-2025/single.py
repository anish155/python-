def single():
    nums=[1,2,3,2,1,4,7,5,4]
    for n in nums:
        if nums.count(n)==1:
            print(n, end=' ')

single()