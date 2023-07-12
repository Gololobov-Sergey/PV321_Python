
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

a = int(input( ))
b = int(input( ))
c = int(input( ))
d = int(input( ))
k = 0
for i in range(4):
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
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print (a)
elif b < c :
    print (b)
else:
    print (c)"""

'''
a = int(input())
b = int(input())
c = int(input())

if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print(a)
'''

'''
l = int(input("Літрів сметани : "))
if l >= 0:
    p = int(input("% сметан для к1 : "))
    if p >= 0 and p <= 100:
        k1 = l * 1000 * p / 100
        if 1000 * l != k1:
            k2 = int(input("мл сметан для к2 : "))
            if k2 <= 1000 * l - k1:
                k3 = 1000 * l - k1 - k2
                if k1 > k3:
                    print("k1 > k3")
                elif k3 > k1:
                    print("k3 > k1")
                else:
                    print("k1 = k3")
            else:
                print("Не вірне значення для к2")
        else:
            print("Після першого більше сметани не було!!")
    else:
        print("Не вірне значення %")
else:
    print("Не вірне значення літрів")

print(k1, k2, k3)
'''

## Дано целое число. Вывести его строку-описание вида «отрицательное чет-
## ное число», «нулевое число», «положительное нечетное число» и т. д.
'''
a = int(input("Число а: "))
if a == 0:
    print("Нульове", end=' ')
else:
    if a > 0:
        print("Додатне", end=' ')
    elif a < 0:
        print("Від'ємне", end=' ')
    
    if a % 2 == 0:
        print("парне", end=' ')
    else:
        print("непарне", end=' ')

print("число")
'''

'''
a = int(input())

if a % 2 == 0:
    print("Парне", end=' ')
else:
    print("Непарне", end=' ')

if a < 10:
    print("однозначне", end=' ')
elif a < 100:
    print("двозначне", end=' ')
else:
    print("трьохзначне", end=' ')

print("число")
'''

## Даны два целых числа: D (день) и M (месяц), определяющие правиль-
## ную дату невисокосного года. Вывести значения D и M для даты, следую-
## щей за указанной.
'''
d = int(input("День   : "))
m = int(input("Місяць : "))

if m == 4 or m == 6 or m == 9 or m == 11:
    dmax = 30
elif m == 2:
    dmax = 28
else:
    dmax = 31

d += 1

if d > dmax:
    d = 1
    m += 1
    m %= 12

print(d, m)
'''


## Даны два целых числа: D (день) и M (месяц), определяющие правиль-
## ную дату невисокосного года. Вывести значения D и M для даты, предше-
## ствующей указанной.
'''
d = int(input("Day:"))
m = int(input("Month:"))

d -= 1

if d == 0:
    m -= 1
    if m == 4 or m == 6 or m == 9 or m == 11:
        dmax = 30
    elif m == 2:
        dmax = 28
    elif m == 0:
        m = 12
        dmax = 31
    else:
        dmax = 31

    d = dmax

print(d, m)
'''


## Локатор ориентирован на одну из сторон света («С» — север, «З» —
## запад, «Ю» — юг, «В» — восток) и может принимать три цифровые ко-
## манды поворота: 1 — поворот налево, –1 — поворот направо, 2 — поворот
## на 180°. Дан символ C — исходная ориентация локатора и целые числа N1
## и N2 — две посланные команды. Вывести ориентацию локатора после вы-
## полнения этих команд.

d = input("Поточна позиція (N, E, S, W) : ")
com1 = int(input("Команда 1 : "))
com2 = int(input("Команда 2 : "))

if d == "N":
    pos = 0
elif d == "W":
    pos = 1
elif d == "S":
    pos = 2
else:
    pos = 3

pos += com1
pos += com2

pos %= 4

if pos == 0:
    d = "N"
elif pos == 1:
    d = "W"
elif pos == 2:
    d = "S"
else:
    d = "E"

print(d)