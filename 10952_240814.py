# 10952
number = ''
while number != '0 0':
    number = input()
    if number == '0 0':
        break
    else:
        print(int(number[0])+int(number[-1]))

# 10952
while True:
    A,B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
