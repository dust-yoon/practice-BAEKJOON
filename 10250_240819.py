# 10250
import sys
input = sys.stdin.readline
case = int(input())

for i in range(case):
    H, W, N = map(int, input().split())
    Y = N % H
    X = N // H + 1
    if N % H == 0:
        Y = H
        X = N // H

    if X <= 9:
        X = '0' + str(X)
    print(str(Y) + str(X))