# 1018 (체스판 다시 칠하기)
    # 시간: 76ms / 코드 길이: 854B
    # count 리스트를 생성하지 않음으로써 공간 확보

import sys
# 원형 체스판은 단 두가지 경우의 수밖에 존재하지 않음
origin_chess_w = [['W', 'B'] * 4, ['B', 'W'] * 4] * 4
origin_chess_b = [['B', 'W'] * 4, ['W', 'B'] * 4] * 4

N, M = map(int, input().split())
chess = []
for _ in range(N):
    new_chess = list(sys.stdin.readline().strip())
    # new_chess = list(input())
    chess.append(new_chess)

min_value = 64

# 8x8 체스판
for k in range(N - 7):
    for l in range(M - 7):
        count_w = 0
        count_b = 0
        for i in range(8):
            for j in range(8):
                if chess[k + i][l + j] != origin_chess_w[i][j]:
                    count_w += 1
                if chess[k + i][l + j] != origin_chess_b[i][j]:
                    count_b += 1

        min_value = min(min_value, count_w, count_b)

print(min_value)

# 외부 정답 1 (설명 참조)
    # 시간: 84ms / 코드 길이: 1008B
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())
    # 시작점 체크 이중 for 문
for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        # 비교 리스트 체크 이중 for 문(홀수)
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 합을 체크하면서 행렬의 홀짝을 한번에 체크 가능해짐
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        # 두가지 경우의 수 중 더 작은 값 count 리스트에 쌓기 
        count.append(min(index1, index2)) 
# 리스트의 값 중에서 가장 작은 값 출력
print(min(count))