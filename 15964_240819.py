# 15964

import sys
input = sys.stdin.readline

def golbang(A, B):
    answer = (A + B)*(A - B)
    return answer

a, b = map(int, input().split())
print(golbang(a, b))
