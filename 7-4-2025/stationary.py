import json

with open('product.json','r')as file:
    data=json.load(file)

items={}
for category in data.values():
    items.update(category)

def products():
    print("the items available are")
    for item,price in items.items():
        print(f"- {item}: Rs {price}")
    order=input("Enter your order:").lower().split(",")
    order=[item.strip() for item in order]
    return order

def bill(order):
    print("\nDUP STATIONARY BILL")
    print("--------------------")
    total=0
    for item in order:
        if item in items:
            print(f"{item} - Rs {items[item]}")
            total+=items[item]
        else:
            print(f"{item} - Not Available")
    print("--------------------")
    print(f"Total: Rs {total}")

order=products()
bill(order)

    
