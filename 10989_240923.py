# 10989 (수 정렬하기 3)

import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001  
# 수의 범위가 0~10,000이므로 10001 크기의 리스트 생성

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)

## 리스트에 수를 저장하려는 방식이 문제가 됨
## 계수 정렬 사용하여 메모리 절약
# N = int(input())
# lst = []

# for _ in range(N):
#     lst.append(int(input()))

# lst.sort()

# for i in lst:
#     print(i)