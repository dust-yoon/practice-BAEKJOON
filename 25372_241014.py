# 25372 (성택이의 은밀한 비밀번호)

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    password = input().strip()

    if 6 <= len(password) <= 9:
        print('yes')
    else:
        print('no')