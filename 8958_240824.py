# 8958
import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    ans = list(input())
    point = 1
    total = 0
    if ans[0] == 'O':
        total += point
    else:
        total += 0
    for i in range(1,len(ans)):
        if ans[i] == 'O':
            if ans[i-1] == 'O':
                point += 1
                total += point
            else:
                point = 1
                total += point
        else:
            total += 0
    print(total)