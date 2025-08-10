import random
def take_num():
    try:
        number=int(input("Enter the number:"))
        return number
    except ValueError:
        print("Please enter a valid number!")
        return None 

def game():
    lives=10
    ans=random.randint(1,100)

    print("Guess the number between 1 and 100! You have 10 lives.")
    
    while lives>0:
        n=take_num()

        if n is None:
            continue

        if (n>ans):
            print("The number is too high.")
            lives-=1
        elif(n<ans):
            print("The number is too low.")
            lives-=1
        elif n==ans:
            print("Congratulations! you have won the guesser.")
            return
        else:
            print("Number out of bounds.")

        
        print(f"Lives remaining: {lives}")

    print(f"💀 Game Over! The correct number was {ans}")

game()
