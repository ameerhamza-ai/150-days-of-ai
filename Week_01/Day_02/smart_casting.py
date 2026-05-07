# code with 3 errors

# age = input("Enter age: ")
# next_year = age + 1
# print("Next year you will be "
# + next_year + " years old")

# Three Errors Fixed

# 1st type error
age = int(input("Enter age: "))
next_year = age + 1

# concatenation error: + operator only use for str contactenation not for int addition
print("Next year you will be "
,next_year , " years old")