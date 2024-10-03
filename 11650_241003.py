# 11650 (좌표 정렬하기)

    # lis = [[1,2],[5,4],[5,1]]
    # lis.sort()
    # print(*lis, end = ' ')

    # li2 = [1, 2, 3,4 ]
    # print(*li2)

import sys

N = int(input())
lst = []
 
for _ in range(N):
    new_lst = list(map(int, sys.stdin.readline().split()))
    lst.append(new_lst)

lst.sort()
for i in range(N):
    print(*lst[i])