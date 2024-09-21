# 1546 (평균)

import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(N):
    score[i] = (score[i] / M) * 100

total = 0
for j in range(N):
    total += score[j]
    
total = total / N
print(round(total, 3))