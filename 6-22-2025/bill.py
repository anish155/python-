class bill():
    def __init__(self,date,product,price):
        self.__date=date
        self.__product=product
        self.__price=price

    def input_date():
        date=input("Enter the date:")
        return date
    
    def input_product():
        prod_list=[]
        while True:
            product=input("Enter the products:")
            prod_list.append(product)
            choice=input("are there any other product you want to buy:")
            if choice.lower()!="y":
                break
        return prod_list
    
    def input_price(num_items):
        price_list=[]
        for i in range(num_items):
            price = float(input(f"Enter price for item {i+1}: "))
            price_list.append(price)
        return price_list
    
    def display(self):
        print(f"\nDate: {self.__date}")
        print("Purchased Items:")
        for i in range(len(self.__product)):
            print(f"  {self.__product[i]} - ${self.__price[i]:.2f}")
        print(f"Total: ${sum(self.__price):.2f}")

date = bill.input_date()
products = bill.input_product()
prices = bill.input_price(len(products))

b=bill(date,products,prices)

b.display()