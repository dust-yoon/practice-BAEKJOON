# 11866 (요세푸스 문제 0)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
stack = deque(i for i in range(1, N+1))
ans = []

for _ in range(N):
    stack.rotate(-K)
    ans.append(stack.pop())

print('<', end="")

for i in range(N-1):
    print(ans[i], end=", ")

print(str(ans[-1]) + '>', end="")