def find_max(a, b, c):
    if a > b and a > c:
        return f"a: {a} is greater"
    elif b > a and b > c:
        return f"b: {b} is greater"
    elif c > a and c > b:
        return f"c: {c} is greater"
    else:
        return "All are equal"

result = find_max(5, 4, 20)
print(result)