def num():
    number=int(input("Enter the number:"))
    return number

def check_palindrome(num):
    pali=num
    rev=0
    rem=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
    if (rev==pali):
        print(f"the number {pali} is a palindrome.")
    else:
        print("it is not a palindrome.")
number=num()
check_palindrome(number)