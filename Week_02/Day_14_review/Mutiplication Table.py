# Multiplication Table Grid (1-5)

# Header row
print("\t", end="")
for i in range(1, 6):
    print(f"{i}\t", end="")
print()
print("-" * 45)

# Table rows
for i in range(1, 6):
    print(f"{i}\t", end="")
    for j in range(1, 6):
        product = i * j
        print(f"{product}\t", end="")
    print()