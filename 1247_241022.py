# 1247 (부호)

import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    stack = []
    for _ in range(N):
        stack.append(int(input()))
    S = sum(stack)
    if S < 0:
        print('-')
    elif S > 0:
        print('+')
    else:
        print(0)