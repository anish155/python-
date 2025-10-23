class Palindrome:
    def __init__(self):
        self.word=None
        self.num=0

    def Input(self):
        self.word=input("Enter the word:")
        self.num=int(input("Enter the number:"))

    def String_Palindrome(self):
        reversed=self.word[::-1]
        if reversed==self.word:
            print("the ",self.word," Palindrome is: ",reversed)
        else:
            print("the ",self.word," Palindrome is not : ",reversed)

    def Num_Palindrome(self):
        rev=0
        temp=self.num

        while temp>0:
            rem=temp%10
            rev=rev*10+rem
            temp//=10

        if rev==self.num:
            print(f"The number {self.num} is a palindrome.")
        else:
            print(f"The number {self.num} is not a palindrome.")

p = Palindrome()
p.Input()
p.String_Palindrome()
p.Num_Palindrome()