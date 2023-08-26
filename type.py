def calculator(operation, a, b):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            if b == 0:
                return "Cannot divide by zero!"
            return a / b
        case _:
            return "Invalid operation"

# Testing
print(calculator("add", 5, 3))        # 8
print(calculator("subtract", 5, 3))   # 2
print(calculator("multiply", 5, 3))   # 15
print(calculator("divide", 5, 3))     # 1.666...
print(calculator("divide", 5, 0))     # Cannot divide by zero!
print(calculator("modulus", 5, 3))    # Invalid operation
