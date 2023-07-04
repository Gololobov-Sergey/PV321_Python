
'''
while condition:
    oper1
    oper1
    oper1
    oper1
'''

'''
a = 5
while a >= 1:
    print(a, end=' ')
    a -= 1
'''

'''
a = int(input("a: "))
b = int(input("b: "))
if a < b:
    while a <= b:
        print(a, end=', ')
        a +=1
else:
    while a >= b:
        print(a, end=', ')
        a -= 1
'''

'''
a = int(input("a: ")) # % //
b = int(input("b: "))
k = 0
while a >= b:
    a -= b
    k += 1
print(k)
'''

'''
a = int(input("a: "))
s = 0
while a > 0:
    r = a % 10
    s += r
    a //= 10

print(s)
'''

'''
a = int(input("a: "))
s = 0
while a > 0:
    r = a % 10
    if r % 2 == 0:
        s += 1
    a //= 10

print(s)
'''

'''
n = int(input("n: "))
k = 1
while k < n:
    k *= 3
if k == n:
    print(True)
else:
    print(False)
'''

'''
n = int(input("n: "))
k = 1
p = 0
while k < n:
    k *= 2
    p += 1
if k == n:
    print(p)
else:
    print("not power 2!")
'''

'''
n = int(input("n: "))
s = 0
i = 1
while i <= n:

    k = 0
    p = i
    while p > 0:
        k += 1
        p //= 10

    m  = 10 ** k * i + i
    print(m, end=" + ")
    s += m
    i += 1
    
print(" =", s)
'''

'''
a = 1
while True:
    print(a)
    a += 1
    if a == 10:
        break
'''

#1 ... 1000
'''
n = int(input("n: "))
i = 2
f = False
while i < n:
    if n % i == 0:
        f = True
        break
    i += 1
if f:
    print("not prime")
else:
    print("prime")
'''

'''
for i in range(10, 21, 2):
    print(i)
'''

'''
n = int(input("Скільки є магазинів : "))
s = 0
for m in range(n):
    h = int(input(f"Кількість холодильників у {m + 1} - му магазині : "))
    s += h
print("Всього", s, "холодильників")
'''

'''
n = int(input("Кількість шкіл:"))
s = 0
for i in range(n):
    u = int(input(f"Учнів у {i + 1} - й школі: "))
    if u > 1000:
        s += 1
print("Кількість шкіл:", s)
'''

'''
n = int(input("Кількість поліклінік : "))
med_personal = 0
for p in range(n):
    print("Поліклініка №", p+1)
    lic = int(input("Лікарі        : "))
    med = int(input("Мед. персонал : "))
    if lic > med:
        med_personal += lic + med
print("Мед працівників : ", med_personal)
'''

'''
#000001 - 999999
count = 0
for i in range(1000, 1000000):
    r1 = i % 10
    r2 = i // 10 % 10
    r3 = i // 100 % 10
    r4 = i // 1000 % 10
    r5 = i // 10000 % 10
    r6 = i // 100000
    if r1 + r2 + r3 == r4 + r5 + r6:
        count += 1
print(count)
'''

'''
s = 0
for i in range(1, 50000):
    r1 = i % 10
    r2 = i // 10 % 10
    r3 = i // 100 % 10
    r4 = i // 1000 % 10
    r5 = i // 10000
    k1 = i % 100
    k2 = i // 10 % 100
    k3 = i // 100 % 100
    k4 = i // 1000
    if r1 == 4 or r2 == 4 or r3 == 4 or r4 == 4 or r5 == 4 or k1 == 13 or k2 == 13 or k3 == 13 or k4 == 13:
        s +=1
print (s)
'''

'''
count = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            h1 = h // 10
            h2 = h % 10
            m1 = m // 10
            m2 = m % 10
            s1 = s // 10
            s2 = s % 10
            if h1 == s2 and h2 == s1 and m1 == m2:
                print(f"{h1}{h2}:{m1}{m2}:{s1}{s2}")
                count += 1
print(count)
'''

'''
print(" Пн Вт Ср Чт Пт Сб Нд")
for d in range(1, 32):
    print(f"{d:3}", end="")
    if d % 7 == 0:
        print()
print()
'''


'''
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {i * n}")
'''

