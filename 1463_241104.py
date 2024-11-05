# 1463 (1로 만들기)
# 전혀 모르겠음 다시 이해 필요

import sys
input = sys.stdin.readline

N = int(input())
def func(N):
    num = 0
    while N != 1:
        if N % 3 == 0:
            N /= 3
            num += 1
            continue
        if N % 2 == 0:
            N /= 2
            num += 1
            continue
        else:
            N -= 1
            num += 1
    return num

print(min(func(N),func(N-1)+1))

# 다시 이해할 필요성 있음 115092 KB / 680 ms / Python 3 / 235 B

n = int(input())
dic = {1: 0, 2: 1}

for i in range(3, n + 1):
    dic[i] = dic[i - 1] + 1
    if i % 3 == 0:
        dic[i] = min(dic[i // 3] + 1, dic[i])
    if i % 2 == 0:
        dic[i] = min(dic[i // 2] + 1, dic[i])

print(dic[n])