# 1966 (프린터 큐)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    line, ans = map(int, input().split())
    stack = deque(map(int, input().split()))
    order = deque([0]*line)
    num = 1 # 순위 입력할때 넣을 숫자
    rotate = 0 # 로테이트 횟수 입력할 num

    while 0 in order:
        A = True
        for i in stack:
            if stack[0] < i:
                A = False
                break
            else:
                continue
        if A:
            stack.popleft()
            stack.append(0)
            order.popleft()
            order.append(num)
            num += 1
            rotate += 1
        else:
            stack.rotate(-1)
            order.rotate(-1)
            rotate += 1

    while rotate % line != 0:
        rotate += 1
        stack.rotate(-1)
        order.rotate(-1)
    
    print(order[ans])

# 예시 1
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    order = [0]*N
    order[M] = 1

    sort_arr = arr.copy()
    sort_arr.sort(reverse=True)

    cnt = 0
    while True:
        if sort_arr[0] == arr[0]:
            cnt += 1
            if order[0] == 1:
                break
            sort_arr.pop(0)
            arr.pop(0)
            order.pop(0)
        else:
            arr.append(arr.pop(0))
            order.append(order.pop(0))

    print(cnt)