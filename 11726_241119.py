# 11726 (2×n 타일링)

import sys
input = sys.stdin.readline
N = int(input())
number = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
if N < len(number):
    print(number[N])
else:
    for i in range(N-len(number)+1):
        i += len(number)
        number.append(0)
        number[i] = number[i-1] + number[i-2]
    print(number[N])