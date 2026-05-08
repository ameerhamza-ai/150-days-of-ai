angle1 = int(input("Enter 1st angle: "))
angle2 = int(input("Enter 2nd angle: "))
angle3 = int(input("Enter 3rd angle: "))
# sum angles
sum_angles = angle1 + angle2 + angle3
# check sum = 180
if sum_angles == 180:
    if angle1 == angle2 and angle2 == angle3:
        print("Equilateral triangle")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalide triangle")

