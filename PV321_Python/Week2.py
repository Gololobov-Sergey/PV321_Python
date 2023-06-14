﻿import math


## - +

#a = 5
#a = -a

#print(a)


## + - * /
#print(5 + 3)
#print(5 - 3)
#print(5 * 3)
#print(5 / 3)

#print(5 + 3)
#print(5. + 3)
#print(5 + 3.)
#print(5. + 3.)


#print((2 + 2) * 2)


#print(2 * 2 ** 3)
#print(2 * 2 * 3)

#print(-5 // 3)

#print(5 % 3)  # 0 1 2 
#print(6 % 3)
#print(7 % 3)
#print(8 % 3)
#print(9 % 3)

#print(3 % 5)

#print(-5.5 % 3)


#a = 5
#b = 4

#a = a + b
#a += b
#print(a)

## += -= *= /= %= //=

#a //= b

#a += 1

## 1. -  2. **  3. * / // %  4. + -


# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
# и BC и их сумму.

'''A = int(input("Введить значення A: "))
B = int(input("Введить значення B: "))
C = int(input("Введить значення C: "))
AC = abs(C - A)
BC = abs(C - B)
Res = AC + BC
print(AC)
print(BC)
print(Res)'''



# Даны координаты двух противоположных вершин прямоугольника:
# (x1, y1), (x2, y2). Стороны прямоугольника параллельны осям координат.
# Найти периметр и площадь данного прямоугольника.

'''x1 = int(input("Введить значення x1: "))
y1 = int(input("Введить значення y1: "))
x2 = int(input("Введить значення x2: "))
y2 = int(input("Введить значення y2: "))
a = abs(x1-x2)
b = abs(y1-y2)
S = a * b
P = 2 * (a + b)
print("S = ", S)
print("P = ", P)'''




# Найти расстояние между двумя точками с заданными координатами
# (x1, y1) и (x2, y2) на плоскости.

'''x1 = int(input("Введить значення x1: "))
y1 = int(input("Введить значення y1: "))
x2 = int(input("Введить значення x2: "))
y2 = int(input("Введить значення y2: "))
a = abs(x1-x2)
b = abs(y1-y2)
l = math.sqrt(a * a + b * b)
print("l = ", l)'''



# Дано двузначное число. Вывести вначале его левую цифру (десятки), 
# а затем — его правую цифру (единицы).

'''n = int(input("Введить число: "))
print(n // 10)
print(n % 10)'''



# С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток.
'''n = int(input("Введить секунди: "))
m = n // 60
print(m)'''




# С начала суток прошло N секунд (N — целое). Найти количество се-
# кунд, прошедших с начала последней минуты.
'''n = int(input("Введить секунди: "))
m = n % 60
print(m)'''


#С начала суток прошло N секунд (N — целое). Найти количество
#полных минут, прошедших с начала последнего часа.
'''n = int(input("Введить секунди: "))
m = (n % 3600)//60
print(m)'''




## Дни недели пронумерованы следующим образом: 0 — воскресенье,
## 1 — понедельник, 2 — вторник, ..., 6 — суббота. Дано целое число K, ле-
## жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
## если известно, что в этом году 1 января было понедельником.

'''K = int(input("Введите число K (1-365): "))
week_day = K % 7
print(f"Номер дня недели для{K} -го дня: {week_day} ")'''




## Дни недели пронумерованы следующим образом: 0 — воскресенье,
## 1 — понедельник, 2 — вторник, ..., 6 — суббота. Дано целое число K, ле-
## жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
## если известно, что в этом году 1 января было четвергом.
'''K = int(input("Введите число K (1-365): "))
week_day = (K + 3) % 7
print(f"Номер дня недели для{K} -го дня: {week_day} ")'''



## Дни недели пронумерованы следующим образом: 1 — понедельник,
## 2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, ле-
## жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
## если известно, что в этом году 1 января было вторником.
'''K = int(input("Введите число K (1-365): "))
week_day = K % 7 + 1
print(f"Номер дня недели для{K} -го дня: {week_day} ")'''


## Дан номер некоторого года (целое положительное число). Опреде-
## лить соответствующий ему номер столетия, учитывая, что, к примеру, на-
## чалом 20 столетия был 1901 год.
'''K = int(input("Введить номер року: "))
st = (K - 1) // 100 + 1
print(f"Сторіччя: {st}")'''



'''print(5 == 5)
print(5 == 4)
print(5 > 5)
print(5 < 4)
print(5 <= 4) # < =
print(5 >= 5) # > =
print(5 != 5) # ! =
print(not 1)'''

'''# or ||
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

# and &&
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()


# xor ^
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)'''



## Дано целое число A. Проверить истинность высказывания: «Число
## A является положительным».

a = int(input())
res = a % 2 == 1
print(res)