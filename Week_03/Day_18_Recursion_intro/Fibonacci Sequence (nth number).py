def fibonacci(n):
    if n <= 1: # Base Case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(f"6th Fibonacci Number: {fibonacci(6)}")