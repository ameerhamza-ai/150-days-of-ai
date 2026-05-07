name = "Ameer"
course = "AI"
gpa = 3.75

# Method 1: + operator
print(name + " studies " + course + " with GPA " + str(gpa))

# Method 2: .format()
print("{} studies {} with GPA {}".format(name, course, gpa))

# Method 3: f-string
print(f"{name} studies {course} with GPA {gpa}")