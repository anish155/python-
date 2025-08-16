class calculator:
    def __init__(self):
        self.__a=0
        self.__b=0

    def take(self):
        self.__a=int(input("Enter the first number:"))
        self.__b=int(input("Enter the second number:"))

    def add(self):
        return self.__a+self.__b
    
    def sub(self):
        return self.__a-self.__b
    
    def multi(self):
        return self.__a*self.__b
    
    def div(self):
        return self.__a/self.__b
    
class Menu(calculator):
    def show_menu(self):
        while True:
            print("\n--- Calculator Menu ---")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice=int(input("Enter your choice:(1 to 5)"))

            if choice == 1:
                self.take()
                print(f"Result: {self.add()}")

            elif choice == 2:
                self.take()
                print(f"Result: {self.sub()}")

            elif choice == 3:
                self.take()
                print(f"Result: {self.multi()}")

            elif choice == 4:
                self.take()
                print(f"Result: {self.div()}")

            elif choice == 5:
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again.")


m=Menu()
m.show_menu()