class calculator:
    def calculate(self,expression):
        try:
            result=eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"

c=calculator()
expr = input("Enter an expression: ")
print(f"Result:{c.calculate(expr)}")