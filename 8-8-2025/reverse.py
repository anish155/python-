def take():
    letter= input("Enter the letter:")
    return letter

def reverse(word):
    reversed=""
    for letters in range(len(word)-1,-1,-1):
        reversed+=word[letters]
    return reversed

word=take()
print(reverse(word))
