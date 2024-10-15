# 1654 (랜선 자르기) 몰라!!!!!!!!!!!

import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

# 이분 탐색 이용
low, high = 1, max(lines)
# 이분 탐색
while low <= high:
    mid = (low + high) // 2  # 중간 값 (랜선의 길이)
    count = sum(line // mid for line in lines)  # mid 길이로 잘랐을 때 얻는 랜선 개수

    if count >= N:  # 필요한 N개의 랜선 이상을 만들 수 있으면
        low = mid + 1  # 더 긴 랜선을 자를 수 있는지 확인
    else:
        high = mid - 1  # 랜선 개수가 부족하니 더 짧게 자름

print(high)  # 최대 길이 출력

# total = 0    
# num = sum(stack) // K
# while total < N:
#     total = 0

#     for i in stack:
#         total += i // num
#     num -= 1

# num += 1

# print(num)
