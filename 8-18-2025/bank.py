class BankAcc:
    def __init__(self):
        self.acc_num = 0
        self.holder_name = None
        self.balance = 0

    def Take(self):
        self.acc_num = int(input("Enter the account number: "))
        self.holder_name = input("Enter the account holder's name: ")
        self.balance = int(input("Enter the account balance: "))

    def Deposit(self, amount):
        if amount <= 0:
            print("❌ Please put a valid amount for deposit.")
            return
        if amount > 500000:
            print("❌ You cannot exceed your monthly limit of 500000.")
            return

        self.balance += amount
        print(f"✅ Your account has been credited with {amount}. New balance = {self.balance}")

    def Withdraw(self, amount):
        if amount <= 0:
            print("❌ Please put a valid amount for withdraw.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return

        self.balance -= amount
        print(f"✅ You withdrew {amount}. Remaining balance = {self.balance}")

    def display_balance(self):
        print("\n--- Account Details ---")
        print(f"Account Number       : {self.acc_num}")
        print(f"Account Holder Name  : {self.holder_name}")
        print(f"Account Balance      : {self.balance}")
        print("------------------------")



ba = BankAcc()
while True:
    print("\n====== Bank Menu ======")
    print("1. Open Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ba.Take()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        ba.Deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        ba.Withdraw(amount)

    elif choice == 4:
        ba.display_balance()

    elif choice == 5:
        print("🙏 Thank you for banking with us!")
        break

    else:
        print("❌ Invalid choice! Please try again.")
