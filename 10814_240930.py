# 10814 (나이순 정렬)

import sys
input = sys.stdin.readline

N = int(input())
member = []

for _ in range(N):
    age, name = map(str, input().split())
    member.append([int(age), name])

member = sorted(member, key = lambda x: x[0])
# member[0].sort()
for i in range(N):
    print(member[i][0], member[i][1])

# * 이차원 리스트 조건 걸어 정렬
# https://dailyheumsi.tistory.com/67