import math

def get_circle_dimensions(radius: float):
  
    # Formula: Area = pi * r^2
    area = math.pi * (radius ** 2)

    # Formula: Circumference = 2 * pi * r
    circumference = 2 * math.pi * radius

    # multi return
    return area, circumference

# Function Call 
r = 5.0
c_area, c_circum = get_circle_dimensions(r)

print(f"Radius: {r}")
print(f"Area: {c_area:.2f}")
print(f"Circumference: {c_circum:.2f}")