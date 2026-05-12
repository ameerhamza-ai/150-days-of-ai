def student_bio(age, university,semester,**details):
    return f"Age: {age}\nUniversity: {university}\nSemester: {semester}\nAdditional Detials: {details}"

result =student_bio(23,"KUST","Second", city = "Kohat", GPA = 3.5)
print(result)
