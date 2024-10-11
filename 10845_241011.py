# 10845 (큐)

import sys
input = sys.stdin.readline
from collections import deque

stack = deque()

N = int(input().strip())

def push(x):
    stack.append(x)
    return

for _ in range(N):
    do = input().strip()

    if 'push' in do:
        num = int(do[5:])
        push(num)
    
    elif 'pop' in do:
        if stack:
            num = stack.popleft()
            print(num)
        else:
            print(-1)
    
    elif 'size' in do:
        print(len(stack))

    elif 'empty' in do:
        if not stack:
            print(1)
        else:
            print(0)

    elif 'front' in do:
        if not stack:
            print(-1)
        else:
            print(stack[0])   

    elif 'back' in do:
        if not stack:
            print(-1)
        else:
            print(stack[-1])