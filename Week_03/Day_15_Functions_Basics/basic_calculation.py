def perform_basic_calculation(a: float, b: float, operator: str):
   
    operator = operator.lower()

    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b != 0: # Division by zero check
            return a / b
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid Operator!"


result = perform_basic_calculation(10, 5, "multiply")
print(f"The result is: {result}")
