# 2028 (자기복제수)

N = int(input())
for i in range(N):
    n = input() # 76
    num = str(int(n)**2) # 5776
    last = num[-len(n):] # 76
    if last == n:
        print('YES')
    else:
        print("NO")