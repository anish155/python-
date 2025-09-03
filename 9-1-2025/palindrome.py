word=input("ENter the letter:")
if word==word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


num=int(input("ENter the number:"))
if str(num)==str(num)[::-1]:
    print(f"{int(num)} is a palindrome.")
else:
    print(f"{int(num)} is not a palindrome.")