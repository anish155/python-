width=float(input("Enter the width:"))
height=float(input("Enter the height:"))
breadth=float(input("Enter the breadth:"))
window=int(input("Enter the size of window:"))
door=int(input("Enter the size of door:"))
price_per=50
room=(2*width+2*breadth+height)-(4*window+door)
current_price=room*price_per
print("price to paint the room:")
print(current_price)