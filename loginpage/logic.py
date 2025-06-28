class Login:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    
    def login_form():
        username=input("Username")
        password=input("password")
        return username,password
    
    def display(self):
        if self.__username=="anish" and self.__password=="anish123":
            print("Login successful")
        else:
            print("unauthorized access revoked.")
        
name,code=Login.login_form()
log=Login(name,code)
log.display()
