from datetime import datetime
class SuperMarket:
    Vat_rate=0.13

    discount = {
        "milk": {"discount": 25, "start": "2025-09-05", "end": "2025-09-10"},
        "bread": {"discount": 20, "start": "2025-09-07", "end": "2025-09-09"},
        "chocolate":{"discount": 50, "start": "2025-09-10", "end": "2025-09-20"}
        }


    def __init__(self):
        self.customer=""
        self.item_name=[]
        self.item_qty=[]
        self.item_price=[]
        self.membership_active=False

    def interface(self):
        print("Super System")
        self.customer=input("Enter the customer name:")
        items=int(input("How many items do you want to buy?"))

        for i in range(items):
            name = input(f"Enter name of item {i+1}: ").lower()
            qty = int(input(f"Enter quantity of {name}: "))
            price = float(input(f"Enter price of {name}: "))

            self.item_name.append(name)
            self.item_qty.append(qty)
            self.item_price.append(price)
    
        self.membership()

    def membership(self):
        ans= input("Do you have membership? (yes/no): ").lower()
        if ans=="yes":
            membership=int(input("Enter your phone number:"))
            mem_price={"Rs:": 150, "start": "2025-09-09", "end": "2026-09-09"}
            
            today=datetime.today().date()
            start_date = datetime.strptime(mem_price["start"], "%Y-%m-%d").date()
            end_date = datetime.strptime(mem_price["end"], "%Y-%m-%d").date()

            if start_date <= today <= end_date:
                print("✅ Membership is active! You will get extra 10% discount on total bill.")
                self.membership_active = True
            else:
                print("❌ Membership expired or not active.")
                self.membership_active = False
        else:
            self.membership_active = False

    def bill_slip(self):
        print("\n===== BILL SLIP =====")
        print(f"Customer name: {self.customer}\n")
        
        subtotal = 0
        for i in range(len(self.item_name)):
            name=self.item_name[i]
            qty=self.item_qty[i]
            price=self.item_price[i]

            amount=qty*price

            if name in SuperMarket.discount:
                discount_info=SuperMarket.discount[name]
                discount_percent=discount_info["discount"]
                discount_amount=(amount*discount_percent)/100
                amount -= discount_amount
                print(f"{name} (x{qty}) = Rs.{amount:.2f} (Discount {discount_percent}% applied)")
            else:
                print(f"{name} (x{qty}) = Rs.{amount:.2f}")

            
            subtotal += amount
            

        vat_amount = subtotal * SuperMarket.Vat_rate
        total = subtotal + vat_amount

        print("-----------------------------")
        print(f"Subtotal: Rs.{subtotal:.2f}")
        print(f"VAT ({SuperMarket.Vat_rate*100:.0f}%): Rs.{vat_amount:.2f}")
        print(f"Total: Rs.{total:.2f}")

        if self.membership_active:
            discount = total * 0.10  
            total -= discount
            print(f"Membership Discount (10%): -Rs.{discount:.2f}")

        print(f"Final Total: Rs.{total:.2f}")

sm=SuperMarket()
sm.interface()
sm.bill_slip()