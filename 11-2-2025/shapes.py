class Shape:
    def __init__(self):
        self.num=0
    
    def Input(self):
        self.num=int(input("Enter the number of * to be made:"))
    
    def Shapes(self):
        for i in range(self.num):
            print("*")
        for i in range(self.num):
            print("*"*i)
        for i in range(self.num):
            print(" "*(self.num-i-1),"*"*i)
        for i in range(self.num):
            print(" "*(self.num-i-1),"*"*(2*i-1))
sh=Shape()
sh.Input()
sh.Shapes()