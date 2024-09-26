# 2738
# 행렬 입력
import sys
N, M = map(int, input().split())
A = []
B = []
C = []
for i in range(M):
      plus = list(map(int, sys.stdin.readline().split()))
      A.append(plus)
for j in range(M):
      plus = list(map(int, sys.stdin.readline().split()))
      B.append(plus)
# 행렬 입력 숫자 합 구하기
for i in range(N):
      C.append([])
      for j in range(M):
            C[i].append(A[i][j] + B[i][j])
# 출력
for i in range(M):
      for j in range(N):
            print(C[i][j], end=" ")
      print()



# for j in range(M) / for i in range(N)

# 1. 반복 줄이고 최대한 간단하게 보내기 
array = [[] * N for _ in range(M)]
# 리스트 컨프리헨션
for k in range(N):
      for q in range(M):
            C[k][q].append(A[k][q] + B[k][q])
print(*C)
# 대체 가능
for l in range(M):
      for t in range(N):
            print(C[l][t], end=" ")
      print()

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
      A.append(list(map(int, input().split())))
for j in range(N):
      B.append(list(map(int, input().split())))

C = [[A[k][q] + B[k][q] for q in range(M)] for k in range(N)]

for i in C:
      print(*i)