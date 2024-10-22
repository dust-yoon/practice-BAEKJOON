# 1264 (모음의 개수)

mo = ('a', 'e', 'i', 'o', 'u')

while True:
    total = 0
    sen = input().lower()
    if sen == '#':
        break
    for i in mo:
        total += sen.count(i)
    print(total)

