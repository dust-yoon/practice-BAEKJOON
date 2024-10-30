# 11047 (동전 0)

# 그리디 알고리즘, 탐욕 알고리즘 관련 설명 필요


# 큐 자료형 - 64ms(메모리:34008KB/코드길이:278B)
import sys
from collections import deque
input = sys.stdin.readline
N, money = map(int, input().split())
coins = deque(int(input()) for _ in range(N))
num = 0
while money:
    coin = coins.pop()
    if money >= coin:
        num += money // coin
        money %= coin
print(num)

# list 자료형 - 36ms(메모리:31120KB/코드길이:243B)
import sys
input = sys.stdin.readline
N, money = map(int, input().split())
coins = [int(input()) for _ in range(N)]
num = 0
while money:
    coin = coins.pop()
    if money >= coin:
        num += money // coin
        money %= coin
print(num)

# 그럼 list에 while 대신 for 문일 경우 - 36ms(메모리:31120KB/코드길이:232B)
import sys
input = sys.stdin.readline
N, money = map(int, input().split())
coins = [int(input()) for _ in range(N)]
num = 0
for coin in coins[::-1]:
    if money >= coin:
        num += money // coin
        money %= coin
print(num)