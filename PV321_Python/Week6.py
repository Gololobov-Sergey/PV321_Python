import string

#print(string.ascii_letters)
#print(string.digits)
#print(string.ascii_lowercase)


import random

#password = ""
#letters = string.ascii_letters + string.digits
#for i in range(8):
#    password += random.choice("abcd")

#print(password)

#st = "Hello Python"

#print(st[2:6])
#print(st[-9:-2])
#print(st[:9])
#print(st[6:])
#print(st[::-1])

st = "Gololobov Sergiy"
#p = st.find(" ")
#st1 = st[p+1:] + " " + st[:p]
#print(st1)




#st = "Full    Cover     Protective  For     Xiaomi Redmi  "
#word = len([i for i in st.split(" ") if i != ""])
#print(word)


#print("dwe", st.center(20), "ewwer")
#print("dwe", st.ljust(20), "ewwer")
#print("dwe", st.rjust(20), "ewwer")
#print(f"Lector {st.zfill(20):>20} is define")
#print(f"Lector {st:^20} is define")
#print(f"Lector {st:>20} is define")
#print()
#print(f"Lector {st} is define")
#print("Lector {0} is define {1}".format(st, 999))
#print()
#c = 201.21545685
#round(c, 2)
#print(f"Lector {c:>20.2f} is define")
#print(f"Lector {round(c, 2):>20.2f} is define")


import re

#pattern = re.compile("^\d+$")
#pattern = re.compile("^\+38\(0\d{2}\)\d{3}-?\d{2}-?\d{2}$")
#pattern = re.compile("^[A-ZА-ЯЇ][a-zа-яї]+ [A-ZА-ЯЇ][a-zа-яї]+$")
pattern = re.compile("^([A-ZА-ЯЇ][a-zа-яї]+ ?){2}$")

# +38(050)123-45-78
#while True:
#   a = input()
#   print(bool(pattern.search(a)))



### LIST ####

#list1 = ["BMW", "Audi", "Mercedes"]
#list2 = list(("BMW", "Audi", "Mercedes"))
#list3 = []

#print(list1)
#print(list2)
#print(list3)

#list4 = [random.randint(10, 20) for i in range(5)]
#print(list4)

#list5 = list("abcdef")
#print(list5)

#list6 = [i for i in list1 if i[0] == "A"]
#print(list6)


#print(list1[1])

#list4 = [random.randint(0, 3) for i in range(10)]
#list4 = [int(input(f"list[{i}] = ")) for i in range(5)]
#print(list4)

#for i in range(list4.count(0)):
#    list4.remove(0)

#print(list4)



'''
maximum = list4[0]
imax = 0
for i in range(len(list4)):
    if list4[i] > maximum:
        maximum = list4[i]
        imax = i

print("imax = ", imax)
print(list4.index(max(list4)))
print(maximum)
print(max(list4))


#list5 = list(list4)
#list5 = list4[:]
list5 = list4.copy()
list5[0] = 999

print(list4)
print(list5)

k = 0
for i in range(len(list4)):
    if list4[i] > 0:
        k += 1

print(k)
'''

'''
list4.append(999)
print(list4)

print(list4.count(0))

list4.extend([444,555,666])
print(list4)

list4 += [222,333,444]
print(list4)

if 999999 in list4:
    list4.index(999999)

list4.insert(2, -666)
print(list4)

list4.pop(2)
print(list4)

list4.remove(555)
print(list4)

list4.sort(reverse=True)
print(list4)
'''

import time

t1 = time.time()

list4 = [random.randint(0, 20) for i in range(1000000)]
#print(list4)
imin = list4.index(min(list4))
imax = list4.index(max(list4))
d = 1

if imin > imax:
    imax, imin = imin, imax

for i in range(imin + 1, imax):
    d *= list4[i]

print(d)

t2 = time.time()
print(t2-t1)