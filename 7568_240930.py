# 7568 (덩치) - 다시

import sys
input = sys.stdin.readline

N = int(input())  # 사람의 수
big = []

# 각 사람의 몸무게와 키를 입력받기
for _ in range(N):
    weight, height = map(int, input().split())
    big.append((weight, height))

print(big)
# 각 사람의 순위를 저장할 리스트
rank = [1] * N

# 모든 사람을 비교하여 순위를 결정
for i in range(N):
    for j in range(N):
        if i != j:
            if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
                rank[i] += 1  # 몸무게와 키가 모두 작으면 순위가 내려감

# 순위 출력
print(' '.join(map(str, rank)))

# import sys
# input = sys.stdin.readline

# N = int(input())
# big = []

# for a in range(N):
#     big.append(list(map(int, input().split())))
#     big[a].append(a+1)

# big.sort(reverse = True)
# key = []

# for b in range(1,N):
#     if b != N-1:
#         if big[b-1][1] >= big[b][1]:
#             pro_key = str(len(key)+1)
#             key.extend(pro_key*(b-len(key)))
#     elif b == N-1:
#         if big[b][1] < big[b+1][1]:
#             pro_key = str(len(key)+1)
#             key.extend(pro_key*(b-len(key)+1))
#         else:
#             pro_key = str(len(key)+1)
#             key.extend(pro_key*(b-len(key)+1))
#             key.extend(len(key)+1)

# print(key)
# # key = [1, 2, 2, 2, 5]
# lst = [0]*N
# for c in range(N):
#     lst[big[c][2]] = key[c]

# print(lst, end = ' ')

# key = []
# bay = key.append(0)
# bay*5
# print(key)
#  key.append(((list(len(key)+1))*(b-len(key))))