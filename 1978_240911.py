# 1978 - 소수찾기

import sys
input = sys.stdin.readline
# N개 주어짐
num = int(input())
n = list(map(int, input().split()))
answer = 0
# [1, 3, 5, 7]
# 소수의 정의 (1 아님, 나눠지는게 나랑 1밖에 없어야 함)
for i in range(num):
    if n[i] != 1:
        total = 0
        for j in range(2 , n[i]):
            if n[i] % j == 0:
                break
            total += 1
        if total == n[i] - 2:
            answer += 1
print(answer)