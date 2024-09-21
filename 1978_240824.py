# 1978
import sys
input = sys.stdin.readline

num = int(input())
n = list(map(int, input().split()))
# 5
# [1, 2, 3, 5, 7]
ans = 0
for i in range(num):
    if n[i] != 1:
        for j in range(2, n[i]):
            if  n[i] % j != 0:
                if j == n[i]-1:
                    ans += 1
                    print(n[i])
                continue
            else:
                break
    else:
        ans += 0
print(ans)