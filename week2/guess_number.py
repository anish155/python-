import random
tries=5
random_number=random.randint(1,10)
while tries>0:
    number=int(input("enter the number:"))
    if(number>random_number):
        print("your number is too high.")
        tries-=1
    elif(number<random_number):
        print("Your number is too low.")
        tries-=1
    else:
        print("you have guessed it right! the number was",random_number)
        break
    print("you have this much tries left:",tries)
if(tries==0):
    print("out of tries better luck next time.")