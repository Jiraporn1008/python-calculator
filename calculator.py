class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b #Fix correct condition

    def multiply(self, a, b):
        result = 0
        negative = b < 0 # Fix for condition is negative
        b = abs(b)
        for i in range(b):
            result = self.add(result, a)
        if negative:
            result = -result
        return result
        

    def divide(self, a, b):
        if b == 0: # Fix for condition is 0
            raise ValueError("Cannot divide by zero")
        result = 0
        while a >= b: #Fix correct condition
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0: # Fix for condition is 0
            raise ValueError("Cannot modulo by zero")
        while a >= b: # Fix correct condition
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))