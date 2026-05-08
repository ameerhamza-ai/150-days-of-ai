item = input("Enter item name: ")
price = int(input("Enter price: "))
qty = int(input("Enter quantity: "))

total = price * qty

print("╔══════════════════════════╗")
print("║     SHOPPING RECEIPT     ║")
print("╠══════════════════════════╣")
print(f"║ Item    : {item:<16}║")
print(f"║ Price   : {price:<13} PKR ║")
print(f"║ Qty     : {qty:<16}║")
print(f"║ Total   : {total:<13} PKR ║")
print("╚══════════════════════════╝")