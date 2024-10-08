# 30802
import sys
input = sys.stdin.readline

ans = 0
num = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
for i in size:
    if i%T == 0:
        ans += i//T
    else:
        ans += (i//T) + 1
print(ans)
print(num // P)
print(num % P)