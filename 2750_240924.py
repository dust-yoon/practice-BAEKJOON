# 2750 (수 정렬하기)

# 1
# 첫째줄에 개수
# 둘째줄에 수 100보다 작거나 같고 중복되지 않음 한 줄에 하나씩 출력

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

lst.sort()

for i in range(N):
    print(lst[i])

# 2
# 리스트 만들어서 맞는 값만 출력

N = int(input())
lst = [0]*2001 # 어차피 수는 -1000~1000
# [0(-1000),0,0,...]
for i in range(N):
    lst[int(input())] += 1
# [1, 1, 1, 0 ,1 ,0,..]
for i in range(2001):
    if lst[i] > 0:
        for _ in range(lst[i]):
            print(i-1000)