# 1764 (듣보잡)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_hear = set(input().strip() for _ in range(N))
set_see = set(input().strip() for _ in range(M))
ans = list(set_hear & set_see)
ans.sort()
print(len(ans))
for i in ans:
    print(i)