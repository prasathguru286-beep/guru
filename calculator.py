def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return None
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    a = float(input("Enter number 1: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Enter number 2: "))

    if op == "+":
        print(f"Result: {add(a, b)}")
    elif op == "-":
        print(f"Result: {subtract(a, b)}")
    elif op == "*":
        print(f"Result: {multiply(a, b)}")
    elif op == "/":
        result = divide(a, b)
        if result is not None:
            print(f"Result: {result}")
    else:
        print("Invalid operator!")

calculator()
