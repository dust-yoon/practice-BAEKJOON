# 2775 (부녀회장이 될테야)

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    m = k + n
    up = 1
    l = k + 1
    down = 1

    for i in range(l):
        up *= (m-i)

    while l != 0:
        down *= l
        l -= 1    

    print(up // down)
