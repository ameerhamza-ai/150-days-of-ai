price = int(input("Enter item price: "))
qty = int(input("Enter quantity: "))
discount = int(input("Enter discount %: "))

subtotal = price * qty
discount_amount = (subtotal * discount) / 100
final_bill = subtotal - discount_amount
tax = final_bill * (17 / 100)
grand_total = final_bill + tax
print("\n================================")
print(f"Subtotal\t\t: {subtotal} PKR")
print(f"Discount\t\t: {discount_amount:.2f} PKR ({discount}%)")
print(f"After Disct\t\t: {final_bill:.2f} PKR")
print(f"GST (17%)\t\t: {tax:.2f} PKR")
print(f"Grand Total\t\t: {grand_total:.2f} PKR")
print("================================")