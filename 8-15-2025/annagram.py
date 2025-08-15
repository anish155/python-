def take():
    word1=input("Enter the letter:")
    word2=input("Enter the letter:")
    return word1, word2

def annagram(w1,w2):
    sort1=sorted(w1)
    sort2=sorted(w2)

    if sort1==sort2:
        print(f"{w1} is a annagram to {w2}.")
    
    else:
        print(f"{w1} is not a annagram to {w2}.")

w1,w2=take()
annagram(w1,w2)