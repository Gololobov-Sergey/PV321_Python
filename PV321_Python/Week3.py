
## Даны координаты поля шахматной доски x, y (целые числа, лежа-
## щие в диапазоне 1–8). Учитывая, что левое нижнее поле доски (1, 1) явля-
## ется черным, проверить истинность высказывания: «Данное поле является
## белым».

"""x = int(input("X = "))
y = int(input("Y = "))
res = (x + y) % 2 == 1
print(res)"""


## Даны целые числа a, b, c. Проверить истинность высказывания:
## «Существует треугольник со сторонами a, b, c».

"""a = int(input())
b = int(input())
c = int(input())
res = a + b > c and a + c > b and b + c > a
print(res)"""

"""
if condition:
    oper1
    oper2
    oper3
else:
    oper4
    oper5
    oper6
"""

"""
a = int(input())
if a > 0:
    print("Positive")
else:
    print("Negative")
"""


"""
a = int(input("Число а: "))
b = int(input("Число b: "))
if b != 0:
    print(a / b)
else:
    print("Error")
"""

"""
a = int(input( ))
b = int(input( ))
c = int(input( ))
d = int(input( ))
k = 0
if a > 0:
    k = k + 1

if b > 0:
    k = k + 1

if c > 0:
    k = k + 1

if d > 0:
    k = k + 1

print(k)
print(4 - k)
"""

"""
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print (a)
elif b < c :
    print (b)
else:
    print (c)"""


a = int(input())
b = int(input())
c = int(input())

if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print(a)