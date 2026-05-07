age = int(input("Enter age: "))
is_student = "True"

if age >= 18 and age <= 60:
    print("Working age!")
else:
    print("Not allowed to work")

    if age >= 13 or is_student == "True":
        print("Can use student discount!")
    else:
        print("Can't use discount")

        if not (age < 18):
            print("Adult!")
        else:
            print("Minor")
