password = input("Enter password: ")

has_length = len(password) >= 8
has_number = any(c.isdigit()
for c in password)
has_upper = any(c.isupper()
for c in password)

if has_length and has_number and has_upper:
    print("Strong password! ")
else:
    print("Weak password! ")
    if not has_length:
        print("→ Too short! Min 8 chars")
        if not has_number:
            print("→ Add a number!")
            if not has_upper:
                print("→ Add uppercase letter!")