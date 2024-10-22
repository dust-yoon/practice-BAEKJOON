# 3003 (킹, 퀸, 룩, 비숍, 나이트, 폰)

import sys
input = sys.stdin.readline

chess_ori = [1, 1, 2, 2, 2, 8]
chess_find = list(map(int, input().split()))
chess_need = []

for i in range(6):
    stack = chess_ori[i] - chess_find[i]
    chess_need.append(stack)

print(*chess_need)