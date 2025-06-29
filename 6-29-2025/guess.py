import random

def your_guess():
    num = int(input("Enter your number (1-100): "))
    return num

def guess():
    rand = random.randint(1, 100)
    attempts = 0

    while True:
        num = your_guess()
        attempts += 1

        if num == rand:
            print(" You guessed it correct! The number was:", rand)
            print("Total attempts:", attempts)
            break
        elif num < rand:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

guess()
