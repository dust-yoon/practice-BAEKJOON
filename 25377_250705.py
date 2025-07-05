# 25377 (빵)
N = int(input())
time = -1
for _ in range(N):
    A,B = map(int, input().split())
    if A<=B:
        if time == -1 or B < time:
            time = B
        else:
            continue
print(time)