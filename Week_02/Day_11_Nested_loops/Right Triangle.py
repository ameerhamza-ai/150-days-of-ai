rows = 5

# Outer loop rows
# Inner loop columns
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()