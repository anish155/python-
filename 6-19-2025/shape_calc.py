class shape():
    def __init__(self,length,breadth=0,height=0):
        self.length=length
        self.breadth=breadth
        self.height=height

class square(shape):
    def __init__(self,length):
        super().__init__(length)

    def len_input():
        length=int(input("Enter the length:"))
        return length
    
    def calc_area(self):
        area=self.length**2
        print(f"the area of square with length {self.length} is {area}.")

    def calc_perimeter(self):
        perimeter=4*self.length
        print(f"the perimeter of square with length {self.length} is {perimeter}")

class rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
    
    def len_input():
        length=int(input("Enter the length:"))
        return length
    
    def bread_input():
        breadth=int(input("Enter the breadth:"))
        return breadth
    
    def calc_area(self):
        area=self.length*self.breadth
        print(f"the area of rectangle with length {self.length} and breadth {self.breadth} is: {area}")
    
    def calc_perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print(f"the area of rectangle with length {self.length} and breadth {self.breadth} is: {perimeter}")

while True:
    print("Shapes")
    print("1. Square")
    print("2. Rectangle")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        length=square.len_input()
        sq=square(length)
        sq.calc_area()
        sq.calc_perimeter()
    
    elif(choice==2):
        length,breadth=rectangle.len_input(),rectangle.bread_input()
        rct=rectangle(length,breadth)
        rct.calc_area()
        rct.calc_perimeter()
    
    else:
        print("Wrong input")
    
    again=input("Do you want to try again ('y' or 'n') ?")
    if(again.lower()!='y'):
        print("Exiting the program.")
        break

    


