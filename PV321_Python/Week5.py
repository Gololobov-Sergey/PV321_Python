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