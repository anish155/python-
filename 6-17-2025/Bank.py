class bank_account():
    def __init__(self,name,account_num,balance):
        self.name=name
        self.account_num=account_num
        self.balance=balance

    def input_detail():
        name=input("Enter your name:")
        account_num=int(input("Enter your account number:"))
        balance=int(input("Enter your bank balance:"))
        return name,account_num,balance
    
    def display(self):
        print("Account details:")
        print("Name:",self.name)
        print("Account Number:",self.account_num)
        print("Account Balance:",self.balance)

class deposit(bank_account):
    def __init__(self,name,account_num,balance,depo):
        super().__init__(name,account_num,balance)
        self.depo=depo

    def saving_amount():
        depo=int(input("Enter the amount of money you want to save:"))
        return depo
    
    def saving(self):
        if(self.depo>0):
            self.balance+=self.depo
            print("Successfully added", self.depo, "to balance. New balance:", self.balance)
        else:
            print("The amount provided is not accountable.")

class withdraw(bank_account):
    def __init__(self,name,account_num,balance,wit):
        super().__init__(name,account_num,balance)
        self.wit=wit

    def retrieve_amount():
        wit=int(input("how much amount do you want to retrieve:"))
        return wit
    
    def retrieving(self):
        if(self.wit>0 and self.wit<=self.balance):
            self.balance-=self.wit
            print("Successfully deducted", self.wit, "from balance. New balance:", self.balance)
        
        else:
            print("Amount exceeded the balance unable to retrieve.")

name,account_num,balance=bank_account.input_detail()

depo_amount = deposit.saving_amount()
d = deposit(name, account_num, balance, depo_amount)
d.saving()
d.display()

wit_amount=withdraw.retrieve_amount()
wit=withdraw(name,account_num,balance,wit_amount)
wit.retrieving()

wit.display()