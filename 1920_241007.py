# 1920 (수 찾기)
    # 50520KB 156ms 229B

import sys

N = int(input())
N_st = set(map(int, sys.stdin.readline().split()))
M = int(input())
M_lst = list(map(int, sys.stdin.readline().split()))

for i in M_lst:
    if i in N_st:
        print(1)
    else:
        print(0)

# for i in (____) 함수의 시간 복잡도
    # list 함수의 경우 시간 복잡도가 O(M): for 문 두번 돌리면 O(MN)
    # set 함수의 경우 시간 복잡도가 O(1)에 그침