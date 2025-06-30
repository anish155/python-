def password():
    word=input("enter the password:")
    return word

def strenght(password):
    nums="0123456789"
    symbol="@#$&~"
    while True:
        if len(password) < 8 or len(password) > 14:
            print("password is not in appropriate length, Try again.")
        elif not any(char in nums for char in password):
            print("your password does not have number please add number to it.")
        elif not any(char in symbol for char in password):
            print("your password does not contain the symbols please add the symbols.")
        elif not any(char.islower() for char in password):
            print("the password must contain atleast one lower case.")
        elif not any(char.isupper() for char in password):
            print("the password must contain atleast one upper case.")
        else:
            print("the password is strong.")
            break
        
        password = input("Enter password again: ")

pwd=password()
strenght(pwd) 
