class node:
    def __init__(self):
        self.lst1=None
        self.lst2=None
    
    def take(self):
        self.lst1=input("Enter data on list 1:").split(",")
        self.lst2=input("Enter data on list 2:").split(",")

    def check(self):
        lst1=[x.strip() for x in self.lst1]
        lst2=[x.strip() for x in self.lst2]

        if len(lst1) != len(lst2):
            return False
        
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
        return True

n=node()
n.take()
print(n.check())