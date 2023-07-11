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




#st = "Full    Cover     Protective  For     Xiaomi Redmi  ".rstrip()
#word = 0
#for i in range(len(st)):
#    if st[i] != " " and st[i+1] == " ":
#        word += 1

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
while True:
   a = input()
   print(bool(pattern.search(a)))
