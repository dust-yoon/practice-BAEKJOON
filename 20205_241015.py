# 20205 (교수님 그림이 깨지는데요?)

import sys
input = sys.stdin.readline

def painting(lst, K):
    new_lst = []
    for i in lst:
        for _ in range(K):
            new_lst.append(i)

    return [new_lst]*K

N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

new_lst = []

for i in range(N):
    new_lst.extend(painting(lst[i], K))

for i in range(N*K):
    print(*new_lst[i])