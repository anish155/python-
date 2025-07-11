class room():
    def length(self):
        len=float(input("enter the width of the room:"))
        return len
    
    def height(self):
        hei=float(input("enter the height of the room:"))
        return hei
    
    def breadth(self):
        bre=float(input("enter the breadth of the room:"))
        return bre
    
    def room_size(self,l,b,h):
        room=2*(l+b)*h
        return room
    
class paint():
    def price_per_room(self,room):
        price=room*10
        return price
    
r=room()
p=paint()
len=r.length()
bre=r.breadth()
hei=r.height()
room_si=r.room_size(len,bre,hei)
print(f"Wall Area: {room_si} square units")
result=p.price_per_room(room_si)
print(f"Paint Price: Rs. {result}")

