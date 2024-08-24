import math
from mod import calculation

def expression(a, b):
    z = 0
    if a >= 15 :
        z = math.sin(2*a) + math.cos(2*b)
    else:
        z = math.sqrt(a + b**2)
    return z

a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
print(f"Значення виразу z = {expression(a, b):.2f}")

n = int(input("Введіть значення n: "))
print(f"Сума числа n: {calculation(n):.2f}")