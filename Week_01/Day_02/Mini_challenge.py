# student result calculator
student_name = input("Enter student name: ")
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

#  total marks
total_marks = m1 + m2 + m3
percentage = (total_marks / 300) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

    print("\n================================")
    print(f"Student\t\t: {student_name}\nTotal\t\t: {total_marks}/300\nPercentage\t: {percentage:.1f}%\nGrade\t\t: {grade}")
    print("=================================")
