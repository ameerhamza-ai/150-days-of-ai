x = "10"
y = "20"
print(x + y)
print(int(x) + int(y))

# both lines have different outputs
# line 1: output "1020" because strings are being concatenated (joined).
# line 2: output "30" because strings are cast to integers for mathematical addition.