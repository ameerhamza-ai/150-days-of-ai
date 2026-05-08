age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Your age is fine, but your weight is below the requirement.")
else:
    print("Sorry, you must be at least 18 years old to donate blood.")
