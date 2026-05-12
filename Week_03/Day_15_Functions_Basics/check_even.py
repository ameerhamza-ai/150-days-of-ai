def is_even(number):
    if number % 2 == 0:
        return f"{number} is even"
    return f"{number} is odd"

result = is_even(15)
print(result)