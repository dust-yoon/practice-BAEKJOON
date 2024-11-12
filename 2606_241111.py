# 2606 (바이러스)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dic = {i : [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visit = set()

def virus(N):
  visit.add(N)
  for virus_friend in dic[N]:
    if virus_friend not in visit:
      virus(virus_friend)

virus(1)
print(len(visit) - 1)