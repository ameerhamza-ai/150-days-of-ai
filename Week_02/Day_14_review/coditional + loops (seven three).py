# SevenThree Loop (1-50)

for i in range(1, 51):
    if i % 7 == 0 and str(i).endswith('3'):
        print("SevenThree")
    elif i % 7 == 0:
        print("Seven")
    elif str(i).endswith('3'):
        print("Three")
    else:
        print(i)