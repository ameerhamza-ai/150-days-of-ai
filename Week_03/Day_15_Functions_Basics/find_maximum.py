def find_max(a, b, c):
    if a > b and a > c:
        return f" a: {a} is greator"
    elif b > a and b > c:
        return f"b: {b} is greator"
    elif c > a and c > b:
        return f"b: {c} is greator"
    else:
        return f"All are equal"
result = find_max(5,4,20)
print(result)