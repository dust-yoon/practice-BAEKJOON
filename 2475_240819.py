# 2475

import sys
input = sys.stdin.readline

number = list(map(int, input().split()))
ans = 0
for i in number:
    ans += i*i
ans %= 10

print(ans)