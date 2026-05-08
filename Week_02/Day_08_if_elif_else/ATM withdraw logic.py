pin = int(input("Enter your PIN: "))
initial_balance = float(input("Enter your initial balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
correct_pin = 1234

if pin == correct_pin:
    if withdraw_amount <= initial_balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")