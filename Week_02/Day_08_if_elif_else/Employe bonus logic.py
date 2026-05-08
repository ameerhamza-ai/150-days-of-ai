salary = int(input("Enter your salary: "))
service = float(input("Enter years of service: "))
bonus = 0

if service > 10:
    bonus = 15
elif service >= 5:
    bonus = 10
    # Yahan hum check kar rahe hain ke service 5 saal se kam hai AUR salary 1 lakh+ hai
elif salary >= 100000 and service < 5:
    bonus = 2
else:
    bonus = 0

    if bonus > 0:
        bonus_amount = (salary * bonus) / 100
        print(f"Congratulations! You got a {bonus}% bonus.")
        print(f"Bonus Amount: {bonus_amount} PKR")
        print(f"Total Salary with Bonus: {salary + bonus_amount} PKR")
    else:
        print("Sorry, no bonus this time. Keep working hard!")