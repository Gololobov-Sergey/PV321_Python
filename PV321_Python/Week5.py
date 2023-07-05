'''
n = int(input())
for k in range(3):
    for i in range(n):
        for j in range(n - 1 - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
'''

'''
print("    |", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print("-" * 45)
for i in range(1, 11):
    print(f"{i:4}|", end="")
    for j in range(1, 11):
        print(f"{i * j : 4}", end='')
    print()
'''

'''
n = int(input())
for i in range(10 ** (n - 1), 10 ** n):
    s = 0
    m = i
    while m > 0:
        r = m % 10
        s += r ** n
        m //= 10
    if s == i:
        print(i)
'''

'''
k = 0
for i in range(10000, 100000):
    k5 = 0
    m = i
    while m > 0:
        r = m % 10
        if r == 5:
            k5 += 1
        m //= 10
    if k5 == 3 and i % 9 == 0:
        print(i, end=", ")
        k += 1
print("\n", k)
'''

'''
n = int(input("Number element : "))
F1 = 1
F2 = 1
k = 2
Fn = 1
while k < n:
    Fn = F1 + F2
    F2 = F1
    F1 = Fn
    k += 1
print(Fn)
'''


'''
a = 0
while a <= 20:
    a += 1
    if a % 2 == 1:
        continue
    print(a)
'''


'''
P = float(input("P = "))
St = 10.0
S = 10.0
k = 1
while S <= 200.0:
    St += St * P / 100.0
    S += St
    k += 1
print(k)
print(S)
'''

'''
s = 0.0
i = 1
n = int(input("Number element : "))
while i <= n:
    p = i
    k = 0
    while p > 0:
        k += 1
        p //= 10

    el = (-1) ** (i-1) * (1 + i/10 ** k)
    print(el, end=" ")
    s += el
    i += 1

print(s)
'''



st = "12245934hello python, c++, , Java3245678"
print(st)
#print(st[-2])

#print(st + " papa")

#print(st[1])


#print(st.capitalize())
#print(st.lower())
#print(st.upper())
#for s in st:
#    print(s.isupper())

print(st.find(",  "))
print(st.rfind(", "))
#print(st.index(",  "))
print(st.count(", "))
print(st.startswith("hell"))
print(st.expandtabs(1))
print(st.strip("1234567890"))
print(st.replace("c++", "C#", 2))
print(st.zfill(50))

print(len(st))
