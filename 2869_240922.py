# 2869 (달팽이는 올라가고 싶다)

import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())

day = math.ceil((v - a) / (a - b)) + 1

# m = v-a
# n = a-b

# if m % n == 0:
#     day = m // n + 1
# else:
#     day = ( v // n) + 1

print(day)

## import math
# 올림 하는 방법 - math.ceil()
# 내림 하는 방법 - math.floor()
# 소수점 버림 하는 방법 - math.trunc()
# 반올림 하는 방법 - round()
# 사사오입 원칙


## task time 너무 길어짐
# snail = a
# day = 1 

# while snail < v:
#     snail -= b
#     day += 1
#     snail += a

# print(day)
