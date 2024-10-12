# 18110 (solved.ac)

import sys
input = sys.stdin.readline

N = int(input())

def round(x):
    x = str(x)
    if '.' in x:
        num, point = map(int, x. split('.'))
        if int(str(point)[0]) >= 5:
            num += 1
        y = num
    else:
        y = x
    return y

stack = []
if not N:
    print(0)
    exit()
M = int(round(N*0.15))
for _ in range(N):
    stack.append(int(input()))
if M:
    stack.sort()
    stack = stack[M:-M]
total = 0
for i in stack:
    total += i
total = total / len(stack)
total = round(total)

print(total)