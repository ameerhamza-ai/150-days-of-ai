def is_even(number):
    if number % 2 == 0:
        return "True"
        #print(f"Even {number} number")
    elif number % 2 != 0:
        return "False"
        #print(f"Odd {number} number")
    else:
         return "Error"

result = is_even(15)
print(f"{result}")

