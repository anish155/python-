def armstrong(num1,num2,num3):
    first=num1**3
    second=num2**3
    third=num3**3
    result=first+second+third
    number=num1*100+num2*10+num3
    print("the armstraong number is:",number)
    print("result is:",result)
    if result==number:
        print("it is armstrong number.")
    else:
        print("it is not.")
armstrong(2,7,6)