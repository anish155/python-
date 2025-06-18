class person():
    def __init__(self,name,address,hobby):
        self.name=name
        self.address=address
        self.hobby=hobby
    
    def form():
        name=input("Enter your name:")
        address=input("Enter your address:")
        hobby=input("Enter your hobby:")
        return name, address, hobby
    
    def info(self):
        print("Person details:")
        print("Name:",self.name)
        print("Address:",self.address)
        print("Hobby:",self.hobby)
    
class friend(person):
    def __init__(self,name,address,hobby,interest):
        super().__init__(name,address,hobby)
        self.interest=interest
    
    def friend_form():
        interest=input("Enter the interest between you and friend:")
        return interest
    
    def friend_info(self):
        print("Friends Info:")
        super().info()
        print("Interest:",self.interest)

class bestfriend(person):
    def __init__(self,name,address,hobby,common_habbit):
        super().__init__(name, address, hobby)
        self.common_habbit = common_habbit

    def bestfriend_form():
        common_habbit = input("Enter your common habit with your best friend: ")
        return common_habbit

    def bestfriend_info(self):
        print("Best Friend Info:")
        super().info()
        print("Common Habit:", self.common_habbit)


n, a, h = person.form()
p = person(n, a, h)
p.info()

print()


n, a, h = person.form()
i = friend.friend_form()
f = friend(n, a, h, i)
f.friend_info()

print()


n, a, h = person.form()
ch = bestfriend.bestfriend_form()
b = bestfriend(n, a, h, ch)
b.bestfriend_info()
    

