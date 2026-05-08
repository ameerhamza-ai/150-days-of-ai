balance = 10000
while True:
    print(f"\nBalance: {balance} PKR")
    print("1. Withdraw  2. Exit")
    choice = input("Choice: ")
    if choice == "2":
        break
    amount = int(input("Amount: "))
    if amount > balance:
        print("Insufficient funds! ")
    else:
        balance -= amount
        print(f"Withdrawn: {amount} ")