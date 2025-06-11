customer={}
def customer_acc_fillup():
    customer["name"]=input("Enter Customer Name:")
    customer["address"]=input("Enter Customer Address:")
    customer["phone"]=int(input("Enter Customer Phone Number:"))
    customer["balance"]=int(input("Enter Customer Bank Balance:"))

def cutomer_acc_details():
    print("/n/t Customer Details:")
    print("Customer name:", customer["name"])
    print("Customer address:", customer["address"])
    print("Customer phone number:", customer["phone"])
    print("Customer bank balance:", customer["balance"])

customer_acc_fillup()
cutomer_acc_details()