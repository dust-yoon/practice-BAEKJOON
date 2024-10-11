# 10816 (숫자 카드 2)

import sys

N = int(input())
N_lst = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in N_lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

M = int(input())
M_lst = list(map(int, sys.stdin.readline().split()))
ans = []

for j in M_lst:
    if j in dic:
        ans.append(dic[j])
    else:
        ans.append(0)

print(*ans)