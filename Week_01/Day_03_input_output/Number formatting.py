num = float(input("Enter number: "))
original = num
rounded = original
decimal_1 = rounded

# Yahan Error tha: Integer mein convert karne ke liye int() function lazmi hai
# Agar int() nahi lagayein ge toh ye float hi rahega
integer = int(decimal_1)

# Output formatting
print(f"Original\t: {original}")
print(f"Rounded\t\t: {rounded:.2f}")
print(f"1 Decimal\t: {decimal_1:.1f}")
print(f"Integer\t\t: {integer}")
