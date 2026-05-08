# Step 1: Inputs
bill_amount = float(input("Enter total bill amount: "))
has_membership = input("Do you have a membership card? (yes/no): ").lower()

# Step 2: initialize discount variable
discount = 0

# Step 3: Main Bill Condition
if bill_amount > 5000:
    discount = 20
    # Nested Condition: Membership check
    if has_membership == "yes":
        discount += 5  # 20 + 5 = 25%

elif bill_amount >= 2000:
     discount = 10
     # Nested Condition: Membership check
     if has_membership == "yes":
         discount += 5  # 10 + 5 = 15%

 # Step 4: Final Calculation
discount_value = (bill_amount * discount) / 100
final_bill = bill_amount - discount_value

print(f"Total Discount: {discount}%")
print(f"Final Amount to Pay: {final_bill} PKR")