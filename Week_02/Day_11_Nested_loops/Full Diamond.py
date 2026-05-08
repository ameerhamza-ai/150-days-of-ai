rows = 5

for i in range(1, rows + 1):
    # Spaces
    for j in range(rows - i):
        print(" ", end="")
        # Stars
    for k in range(i):
        print("* ", end="")
    print()
      
for i in range(rows - 1, 0, -1):
    # Spaces
    for j in range(rows - i):
        print(" ", end="")
    # Stars
    for k in range(i):
        print("* ", end="")
    print()