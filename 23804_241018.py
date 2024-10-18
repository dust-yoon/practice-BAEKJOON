# 23804 (골뱅이 찍기 - ㄷ)

N = int(input())
sen = '@@@@@'*N
for _ in range(N):
    print(sen)
column = '@'*N
for _ in range(N*3):
    print(column)
for _ in range(N):
    print(sen)