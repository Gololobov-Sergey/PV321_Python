
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