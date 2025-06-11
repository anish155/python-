def simple_search(arr,target):
    tries=4
    for i in range(len(arr)):
        if arr[i]==target:
            print("the number was",i)
            break
        else:
            print("the guessed number is wrong")
            tries-=1
        print("you have this much tries left:",tries)
simple_search([10,12,34,56,100],56)