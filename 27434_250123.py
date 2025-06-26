# 27434 (팩토리얼 3)

N = int(input())
if N == 1 or 0:
    print(1)
else:
    n = 1
    for i in range(1,N+1):
        n*=i
    print(n)