# 1018 (체스판 다시 칠하기)

import sys
input = sys.stdin.readline()

N, M = map(int, input().split())
chess = []

for _ in range(N):
    new_chess = list(input())
    chess.append(new_chess)

# place = chess[i][j]
# place_up = chess[i-1][j]
# place_right = chess[i][j+1]
# place_left = chess[i][j-1]
# place_down = chess[i+1][j]
chess_choice = [[],[],[],[],[],[],[],[]]

while True:
    k = 0
    l = 0
    for i in range(8):
        for j in range(8):
            chess_choice.append(chess[i+k][j+l])
    # 새로운 체스판 생성

print(chess_choice)
string = 'BWBWBBWBBWWBBWBWB'
lst = list(string)
print(lst)