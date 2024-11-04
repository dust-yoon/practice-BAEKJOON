# 17219 (비밀번호 찾기)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = dict()

for _ in range(N):
    site, word = map(str, input().split())
    password[site] = word

for _ in range(M):
    print(password[input().strip()])