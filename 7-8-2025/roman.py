class solution():
    def roman(self):
        letter=input("Enter your roman letter:").upper()
        return letter
    
    def convert(self,number):
        roman_values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "c":100,
            "D":500,
            "M":1000
        }
        if number in roman_values:
                print(f"the value of roman letter {number} is {roman_values[number]}")
        else:
             print("Invalid roman letter.")


s=solution()
num=s.roman()
s.convert(num)