num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 > num2:
    print(f"1st number is greater: {num1}")
elif num1 == num2:
    print("Both are equal")
else:
    print(f"2nd is greater: {num2}")

    if num1 == (num2 * 2):
        print("First number is double of the second!")
