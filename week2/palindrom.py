number=121
pali=number
rem=0
rev=0
while(number!=0):
    rem=number%10
    rev=rev*10+rem
    number=number//10
print(rev)
if(rev==pali):
    print("it is palindrome.")
else:
    print("not a palindrome.")