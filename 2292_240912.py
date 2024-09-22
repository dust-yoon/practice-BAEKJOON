# 2292
import sys
input = sys.stdin.readline

N = int(input())
N = N - 1
d = 0

while N > 0:
    d += 1
    N -= 6*d

print(d + 1)

# [1 + [i*6 for i in range()]]
#  < N <
#    [1 + [(i+1)*6 for i in range()]]