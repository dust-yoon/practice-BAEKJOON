# 2231(생성자 구하기 어려움)

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N+1):
    total = sum((map(int, str(i))))
    num = N - total
    if num == i:
        print(i)
        break
    if i == N:
        print(0)