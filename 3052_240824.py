# 3052
import sys
input = sys.stdin.readline

lst = []
rest = {}
ans = 0
for k in range(42):
    rest[k] = 0
for i in range(10):
    lst.append(int(input()))
    rest[lst[i]%42] += 1
for k in range(42):
    if rest[k] != 0:
        ans += 1
print(ans)