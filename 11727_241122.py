# 11727 (2×n 타일링 2)

import sys
input = sys.stdin.readline

N = int(input())
number = [0, 1, 3, 5, 11, 21, 43, 85, 171]
k = len(number)
if N < k:
    ans = number[N]
else:
    number.extend([0]*(N-k+1))
    for i in range(N-k+1):
        i += k
        if i%2:
            number[i] = number[i-1]*2 - 1
        else:
            number[i] = number[i-1]*2 + 1
    ans = number[N]

print(ans%10007)