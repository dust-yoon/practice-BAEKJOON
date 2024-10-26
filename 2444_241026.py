# 2444 (별 찍기 - 7)

N = int(input())

for i in range(N-1):
    print(' '*(N-1-i), end='')
    print('*'*(2*i+1))
for i in range(N):
    print(' '*(i), end='')
    print('*'*(2*(N-i)-1))
