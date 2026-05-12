def sum_all_numbers(*marks):
    total = sum(marks)
    return f"Sum: {total}"

result = sum_all_numbers(34,67,89,67,45)
print(result)