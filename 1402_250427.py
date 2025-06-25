# 1402 (아무래도이문제는A번난이도인것같다)
# 32544 KB / 40 ms / 319 B 

import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    A = True
        
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print("yes")