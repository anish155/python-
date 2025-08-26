class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,insert):
        self.items.append(insert)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.peek())   
print("Popped:", s.pop())         
print("Stack size:", s.size())    
print("Is empty?", s.is_empty())  

