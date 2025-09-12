class system:
    def __init__(self):
        self.name=[]
        self.address=[]
    def Take(self):
        print("System intake")
        for i in range(5):
            name=input("Enter the registerate nanes:")
            address=input("Enter the registrate address:")
            self.name.append(name)
            self.address.append(address)
            
     def Find(self):
         search = input("Enter name to search: ")
         if search in self.name:
            index = self.name.index(search)
            print(f"Address of {search}: {self.address[index]}")
         else:
            print(f"{search} not found in records.")         
            
sys=system()              
sys.Take()
sys.Find()
