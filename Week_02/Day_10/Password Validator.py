password = "kust2024"
while True:
    attempt = input("Enter password: ")
    if attempt == password:
        print("Access granted! ")
        break
    print("Wrong! Try again ")
