# 10802 (369 게임)

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
time = 0
for i in range(A, B+1):
    if i % 3 == 0:
        time += 1
    else:
        if '3' in str(i):
            time += 1
        elif '6' in str(i):
            time += 1
        elif '9' in str(i):
            time += 1
print(time%20150523)

# 17 r r 20 r 22 r r 25 r r 28 r r(30) 

# 시간초과 남
A, B = map(int, input().split())
time = 0
for i in range(A, B+1):
    if '3' in str(i):
        time += 1
    elif '6' in str(i):
        time += 1
    elif '9' in str(i):
        time += 1
print(time%20150523)