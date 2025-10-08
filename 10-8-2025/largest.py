class Large:
    def __init__(self):
        self.nums=[]
    
    def Take(self):
        print("entering the numbers:")
        for _ in range(5):
            num=int(input("Enter the number in list:"))
            self.nums.append(num)
        
    def Largest(self):
        first=self.nums[0]
        for num in self.nums:
            if num>first:
                first=num
        print("Largest number is:", first)
            
L=Large()
L.Take()
L.Largest()