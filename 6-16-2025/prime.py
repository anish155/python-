class prime:
    def __init__(self,num):
        self.num=num

    def take_num():
        num=int(input("enter the number:"))
        return num

    def check_prime(num):
        if(num<2):
            print("the number is not a prime number")
            return
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                print("the number is not a prime.")
                return 
            else:
                print("the number is a prime.")
                return 
number=prime.take_num()
prime.check_prime(number)  

