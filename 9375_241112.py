# 9375 (패션왕 신해빈)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        name, category = map(str, input().split())
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
    case = 1
    for i in dic:
        case *= dic[i]+1
    print(case-1)