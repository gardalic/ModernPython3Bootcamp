def add(a, b):
    return a + b

def math(a, b, fn=add):
    return fn(a, b)

def substract(a, b):
    return a - b

print(f"2 + 2 is {math(2, 2)}")
print(f"2 - 2 is {math(2, 2, substract)}")
