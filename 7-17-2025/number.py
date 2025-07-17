import random
answer=random.randint(1,100)
life=5
while True:
    user_choice=int(input("Enter the number you think is the one:"))
    if user_choice == 0:
        print("The number zero cannot be touched.")
        continue
    
    if user_choice == answer:
        print("🎉 You have guessed correct!")
        break
    elif user_choice < answer:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    life -= 1
    if life == 0:
        print("Too bad! Out of moves. Try your luck next time, noob.")
        print(f"The correct answer was: {answer}")
        break
    else:
        print(f"Lives remaining: {life}")


