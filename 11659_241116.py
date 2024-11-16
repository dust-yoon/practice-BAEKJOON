# 11659 (구간 합 구하기 4)
import time
import sys
from time import strftime
start_time = time.time()

input = sys.stdin.readline

N, T = map(int, input().split())
range_num = dict(map(int, input().split()))
print(range_num)

for _ in range(T):
    i, k = map(int, input().split())
    new_num = range_num[i-1:k]
    print(sum(new_num))

print(time.time() - start_time)

# 누적합을 이용한 문제 해결

import sys
input = sys.stdin.readline

# 누적합 부분 암기, 이해

def cum_sum(arr):
    cumsum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        cumsum[i+1] = cumsum[i] + arr[i]
    return cum_sum

# 누적합 부분 끝

N, T = map(int, input().split())
range_num = list(map(int, input().split()))
cumsum = cum_sum(range_num)
for _ in range(T):
    i, k = map(int, input().split())
    answer = cumsum[k] - cumsum[i-1]
    print(answer)