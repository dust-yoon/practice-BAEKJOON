# 13277 (큰 수 곱셈)

import sys
a, b = map(int, sys.stdin.readline().split())
print(a*b)


# 시간 줄이는법 참조
from decimal import MAX_PREC, Decimal, getcontext

getcontext().prec = MAX_PREC
a, b = map(Decimal, input().split())
print(a * b)