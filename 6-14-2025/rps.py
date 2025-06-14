import random as r
move=input("Enter your move:").lower()
actual_move=["r","p","s"]
comp_move=r.choice(actual_move)

print("Computer chose:", comp_move)

if(comp_move==move):
    print("It is a draw.")
elif (comp_move == 'r' and move == 's') or \
     (comp_move == 'p' and move == 'r') or \
     (comp_move == 's' and move == 'p'):
    print("You lost!")
else:
    print("You won!")
