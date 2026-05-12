def find_maximum_value(*numbers):
    if not numbers:
        return "No numbers provided"
    return f"Maximum: {max(numbers)}"

result = find_maximum_value(45, 89, 23, 102, 67)
print(result)