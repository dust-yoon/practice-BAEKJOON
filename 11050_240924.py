# 11050 (이항계수 1)

n, k = map(int, input().split())
up = 1
down = 1


for i in range(k):
    up *= (n-i)
    down *= (i+1)

num = int(up/down)
print(num)