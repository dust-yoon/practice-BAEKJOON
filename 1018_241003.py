# 1018 (체스판 다시 칠하기)

import sys

# 원형 체스판은 단 두가지 경우의 수밖에 존재하지 않음
origin_chess = [['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W']]

N, M = map(int, input().split())
chess = []
for _ in range(N):
    new_chess = list(sys.stdin.readline().strip())
    # new_chess = list(input())
    chess.append(new_chess)

A = True
k = 0 # 세로 N
l = 0 # 가로 M
min_value = 64

while A:
    value = 0
    for i in range(8):
        for j in range(8):
            if origin_chess[i][j] != chess[i+k][j+l]:
                value += 1
            else:
                continue

    min_val = min(value, 64-value)
    min_value = min(min_val, min_value)

    if l + 8 < M:
        l += 1
        if l + 7 == M and k + 7 < N:
            k += 1

    if k+7 == N or min_value == 0:
        A = False

print(min_value)

    # if value <= 32:
    #     min_val = value
    # else:
    #     min_val = 64 - value

    # if min_val < min_value:
    #     min_value = min_val