class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_Node=Node(data)
        if not self.head:
            self.head=new_Node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_Node
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


l=Linked()
l.insert(10)
l.insert(20)
l.insert(30)
l.display()