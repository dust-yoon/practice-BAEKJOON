# 11727 (2×n 타일링 2)

import sys
input = sys.stdin.readline
N = int(input())
number = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
k = len(number)
if N < len(number):
    ans = number[N]
else:
    number.extend([0]*(N-k+1))
    for i in range(N-k+1):
        i += k
        number[i] = number[i-1] + number[i-2]
    ans = number[N]




print(ans%10007) 