# 2744
r = ""
for i in input():
    if i.islower():
        r += i.upper()
    else:
        r += i.lower()
print(r)

r = ""
for i in input():
    r += i.upper() if i.islower() else i.lower()
print(r)