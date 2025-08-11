def flatten():
    nested=[1,[2,[3,4],5],6]
    flattened=[]

    def helper(lst):
        for item in lst:
            if isinstance(item,list):
                helper(item)
            else:
                flattened.append(item)
    helper(nested)
    return flattened

print(flatten())