def calculate_total_bill(**items):
    total = sum(items.values())
    return f"Total Bill: {total}"

result = calculate_total_bill(Laptop=150000, Mouse=2000, Keyboard=5000)
print(result)