import math

def expression(a, b):
    z = 0
    if a >= 15 :
        z = math.sin(2*a) + math.cos(2*b)
    else:
        z = math.sqrt(a + b**2)
    return z

def product(x, y):
    dob = 1
    for i in range(x, y + 1):
        if i % 2 == 1:
            dob *= i
    return dob

def calculation(n):
    sum = 0
    for val in range(1, n + 1):
        sum += (val+1)/val
    return sum

a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
print("Значення виразу z = ", expression(a, b))

n = int(input("Введіть значення n: "))
print(f"Сума числа n={n}:", calculation(n))