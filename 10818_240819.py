# 10818
import sys
input = sys.stdin.readline
time = int(input())
number = list(map(int, input().split()))

mini = min(number)
maxi = max(number)

print(mini, maxi)