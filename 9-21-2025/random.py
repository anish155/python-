import random

low,high=1,100

print("Think of the guessing number in range of 1 to 100:")

while True:
    guess=(low+high)//2
    print(f"My guess: {guess}")
    feedback = input("Too (H)igh, (L)ow, or (C)orrect? ").lower()
    if feedback=="c":
        print("Yay! I guessed it 🎉")
        break

    elif feedback=="h":
        high=guess-1

    elif feedback=="l":
        low=guess+1

    else:
        print("Please enter H, L, or C!")
