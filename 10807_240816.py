# 10807
import sys
N = int(input())
num = list(map(int, sys.stdin.readline().split()))
number = int(input())
count = {number:0}

for i in range(N):
    if num[i] == number:
            count[number] += 1

print(count[number])