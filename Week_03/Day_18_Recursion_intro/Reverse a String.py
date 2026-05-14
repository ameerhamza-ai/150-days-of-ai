def reverse_string(s):
    if len(s) == 0: # Base Case
        return s
    return reverse_string(s[1:]) + s[0]
print(f"Reverse of 'Python': {reverse_string('Python')}")