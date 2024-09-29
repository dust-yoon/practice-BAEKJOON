# 2798 (블랙잭)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
k = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for l in range(j+1, N):
            plus = lst[i] + lst[j] + lst[l]

            if plus > k and plus < M:
                k = plus
            if plus == M:
                k = M
                break
            if plus > M:
                continue

print(k)

