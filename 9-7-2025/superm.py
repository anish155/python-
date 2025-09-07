class SuperMarket:
    Vat_rate=0.13

    def __init__(self):
        self.customer=""
        self.item_name=[]
        self.item_qty=[]
        self.item_price=[]

    def interface(self):
        print("Super System")
        self.customer=input("Enter the customer name:")
        items=int(input("How many items do you want to buy?"))

        for i in range(items):
            name = input(f"Enter name of item {i+1}: ")
            qty = int(input(f"Enter quantity of {name}: "))
            price = float(input(f"Enter price of {name}: "))

            self.item_name.append(name)
            self.item_qty.append(qty)
            self.item_price.append(price)


    def bill_slip(self):
        print("\n===== BILL SLIP =====")
        print(f"Customer name: {self.customer}\n")
        
        subtotal = 0
        for i in range(len(self.item_name)):
            amount = self.item_qty[i] * self.item_price[i]
            subtotal += amount
            print(f"{self.item_name[i]} (x{self.item_qty[i]}) = Rs.{amount:.2f}")

        vat_amount = subtotal * SuperMarket.Vat_rate
        total = subtotal + vat_amount

        print("-----------------------------")
        print(f"Subtotal: Rs.{subtotal:.2f}")
        print(f"VAT ({SuperMarket.Vat_rate*100:.0f}%): Rs.{vat_amount:.2f}")
        print(f"Total: Rs.{total:.2f}")

sm=SuperMarket()
sm.interface()
sm.bill_slip()