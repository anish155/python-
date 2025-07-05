def word():
    letter=input("enter the word:")
    return letter
def reverse(word):
    reversed=word[::-1].strip(" ")
    print(reversed)

letter=word()
reverse(letter)