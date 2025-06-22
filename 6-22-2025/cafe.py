class Cafe:
    def __init__(self):
        self.__drink_items = [
            ("Cappuccino", 150),
            ("Americano", 140),
            ("Latte", 160),
            ("Frappe", 130),
            ("Boba tea", 200)
        ]
        self.__baked_items = [
            ("Doughnut", 50),
            ("Cookies", 90),
            ("Pastry", 150)
        ]
        self.__orders = []  # To keep track of what customer buys

    def display_menu(self):
        print("\n--- Drinks Menu ---")
        for i, (name, price) in enumerate(self.__drink_items, 1):
            print(f"{i}. {name} - Rs. {price}")
        
        print("\n--- Bakery Menu ---")
        for i, (name, price) in enumerate(self.__baked_items, 1):
            print(f"{i}. {name} - Rs. {price}")

    def customer_order(self):
        while True:
            print("\nOptions:")
            print("1. Drinks")
            print("2. Baked Items")
            choice = int(input("Enter the option (1 or 2): "))
            
            if choice == 1:
                self.display_menu()  # optional: show menu again
                order = input("Which beverage do you want today? ")
                found = False
                for item, price in self.__drink_items:
                    if item.lower() == order.lower():
                        self.__orders.append((item, price))
                        found = True
                        break
                if not found:
                    print("Drink not found.")
            
            elif choice == 2:
                self.display_menu()
                order = input("Which baked item do you want today? ")
                found = False
                for item, price in self.__baked_items:
                    if item.lower() == order.lower():
                        self.__orders.append((item, price))
                        found = True
                        break
                if not found:
                    print("Baked item not found.")
            
            else:
                print("Invalid option.")

            extra = input("Do you want to order more items? (y/n): ")
            if extra.lower() != "y":
                print("That's all. Thank you for buying!\n")
                break

    def bill(self):
        print("\n--- Your Bill ---")
        total = 0
        for item, price in self.__orders:
            print(f"{item}: Rs. {price}")
            total += price
        print(f"Total Amount: Rs. {total}")


# Driver code
c = Cafe()
c.display_menu()
c.customer_order()
c.bill()
