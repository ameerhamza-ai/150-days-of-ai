numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Square them
squared = map(lambda x: x**2, evens)

# Step 3: Sort descending
final_result = sorted(squared, reverse=True)

print(final_result)  