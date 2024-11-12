# 9095 (1, 2, 3 더하기)
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 4
dp[1], dp[2], dp[3] = 1, 2, 4
total = 0
for _ in range(N):
    M = int(input())
    if len(dp) <= M:
        
        for i in range(len(dp), M+1):
            dp.extend([0]*(M+1-len(dp)))
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[M])
    else:
        print(dp[M])


# 9095 (틀린 답)
import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    M = int(input())
    time = 0
    number = {1: 0, 2: 0, 3: M//3}
    for _ in range(0,(M//3)+1):
        total = 1
        rest = M - 3*(number[3]) 
        number[2] = rest//2
        while number[2] >= 0 and number[1] != rest:
            total = 1
            number[1] = M - 3*(number[3]) - 2*(number[2])
            for i in range(1, number[1]+number[2]+number[3]+1):
                total *= i
            for j in range(1,4):
                if number[j] >= 2:
                    for k in range(1, number[j]+1):
                        total /= k
            time += int(total)
            number[2] -= 1
        number[3] -= 1

    print(time)

# 4 -> 7
# 7 -> 44
# 10 -> 274

# 1 1
# 2 2
# 3 4
# 4 7
# 5 13
# 6 24
# 7
# 8 81