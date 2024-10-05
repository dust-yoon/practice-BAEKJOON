# 11651 (좌표 정렬하기 2)

import sys

N = int(input())
lst = []

for _ in range(N):
    new_lst = tuple(map(int, sys.stdin.readline().split()))
    lst.append(new_lst)

# 이차원 리스트 다조건 나열 참조
lst = sorted(lst, key = lambda y : (y[1], y[0]))
for i in range(N):
    num = lst[i]
    print(*num)