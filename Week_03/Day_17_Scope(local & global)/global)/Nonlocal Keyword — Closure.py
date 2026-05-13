def count():
    c = 0
    def increment():
        nonlocal c
        c += 1
        return c
    return increment
counter = count()
print(counter())
print(counter())