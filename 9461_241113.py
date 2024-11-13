# 9461 (파도반 수열)

import sys
input = sys.stdin.readline
# 넣었을때 4ms 절감

T = int(input())
P = [0,1,1,1,2]
for _ in range(T):
    N = int(input())
    k = len(P)
    if N >= k:
        P.extend([0] * (N + 1 - len(P)))
        for i in range(k, N+1):
            P[i] = P[i-2] + P[i-3]
    print(P[N])