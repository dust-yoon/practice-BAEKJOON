# # 11399 (ATM)

import sys
input = sys.stdin.readline

N = (int(input()))
lst = list(map(int, input().split()))
lst.sort(reverse=True)
total = 0

for i in range(N, 0,-1):
    total += lst.pop()*i

print(total)