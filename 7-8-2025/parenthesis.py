class check():
    def paranthesis(self):
        symbol=input("Enter the symbol:")
        return symbol
    
    def check(self,data):
        paranthesis=["{}","[]","()"]
        if data in paranthesis:
            return True
        else:
            return False
            
c=check()
data=c.paranthesis()
result=c.check(data)
print(result)
