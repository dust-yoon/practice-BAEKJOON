# 10951
while True:
    number = input()
    if bool(number) == False:
        break
    else:
        print(int(number[0])+int(number[-1]))

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break

# number = input()
# print(bool(number))