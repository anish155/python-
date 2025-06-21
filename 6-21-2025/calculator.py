class calculator():
    def __init__(self,num1,num2):
        self.__num1=num1
        self.__num2=num2

    def input_num():
        num1=int(input("Enter the number:"))
        num2=int(input("Enter the second number:"))
        return num1,num2
    
    def addition(self):
        add=self.__num1+self.__num2
        return add
    
    def subtraction(self):
        sub=self.__num1-self.__num2
        return sub
    
    def multiply(self):
        pro=self.__num1*self.__num2
        return pro
    
    def division(self):
        try:
            div = self.__num1 / self.__num2
            return float(div)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return None
        

while True:
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter the calculation you want:"))
    if choice in [1,2,3,4]:
        n1,n2=calculator.input_num()
        calc=calculator(n1,n2)

        result=(
            calc.addition() if choice==1 else
            calc.subtraction() if choice==2 else
            calc.multiply() if choice ==3 else
            calc.division() 
        )
        print("Result:", result)

    elif choice==5:
        print("exiting program")
        break
    else:
        print("invalid choice.")
