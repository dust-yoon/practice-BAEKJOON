# 10773 (제로)

import sys
input = sys.stdin.readline

K = int(input().strip())
real_lst = []

for _ in range(K):
    N = int(input().strip())
    if N:
        real_lst.append(N)
    else:
        real_lst.pop()

total = 0

for _ in range(len(real_lst)):
    total += real_lst.pop()

print(total)