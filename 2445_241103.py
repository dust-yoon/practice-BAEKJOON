# 2445 (별 찍기 - 8)

N = int(input())

for i in range(N):
    print('*'*(i+1), end='')
    print(' '*(N-1-i)*2, end='')
    print('*'*(i+1))
for i in range(N-1):
    print('*'*(N-1-i), end='')
    print(' '*(i+1)*2, end='')
    print('*'*(N-1-i))