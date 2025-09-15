# 27433 (팩토리얼 2)

total = 1
N=int(input())
if N==0:
    print(1)
else:
    for i in range(N):
        total*=(i+1)
    print(total)
