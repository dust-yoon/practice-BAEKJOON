# 2443 (별 찍기 - 6)

N = int(input())

for i in range(N):
    print(' '*(i), end='')
    print('*'*(2*(N-i)-1))
