# 2609 (최대공약수와 최소공배수 / GCD & LCM)

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, gcd_value):
    return (a * b) // gcd_value

a, b = map(int, input().split())

gcd_value = gcd(a, b)
lcm_value = lcm(a, b, gcd_value)

print(gcd_value)
print(lcm_value)

# lst = list(map(int, input().split()))
# b = max(lst)
# s = min(lst)

# for i in range(s, 0, -1):
#     if s % i == 0 and b % i == 0:
#         print(i)
#         break

# while True:
#     j = m
#     if j % m == 0 and j % n == 0:
#         print(j)
#         break
#     j += m