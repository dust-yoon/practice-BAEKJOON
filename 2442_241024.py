# 2442 (별 찍기 - 5)

N = int(input())

for i in range(N):
    print(' '*(N-1-i), end='')
    print('*'*(2*i+1))
