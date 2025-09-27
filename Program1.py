class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def operate(self, operation: str) -> float:
        operation = operation.lower()
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            return self.a / self.b if self.b != 0 else "Error: Division by zero"
        else:
            return "Invalid operation"
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ")
calc = Calculator(a, b)
print("Result:", calc.operate(op))