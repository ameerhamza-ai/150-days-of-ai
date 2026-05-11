def get_grade(marks):
    if marks >= 90:
        return f"Marks = {marks}\nGrade: A+"
    elif marks >= 80:
        return f"Marks = {marks}\nGrade: A"
    elif marks >= 70:
        return f"Marks = {marks}\nGrade: B"
    else:
        return f"Marks = {marks}\nGrade: Fail"

result = get_grade(60)
print(result)