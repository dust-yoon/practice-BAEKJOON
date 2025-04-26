# 9070 (장보기)
# 32412 KB / 88 ms / 253 B 

T = int(input())
for _ in range(T):
    n = int(input())
    ratio = []
    for i in range(n):
        wei, won = map(int, input().split())
        ratio.append([won, wei/won])
    ratio = sorted(ratio, key=lambda x: (-x[1],x[0]))
    print(ratio[0][0])


# 딕셔너리 다중조건 정렬 lambda 이용