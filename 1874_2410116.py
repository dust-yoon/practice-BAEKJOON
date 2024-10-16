# 스택 수열

import sys
from collections import deque

N = int(input())
num = deque(range(1, N+1))
goal = deque(input() for _ in range(N))

num_lst = [1]
stack = deque()
ans = []

while True:
    
    if goal[0] != num_lst[-1]:
        if num_lst[-1] < N:
            num_lst.append(num_lst[-1]+1)
            ans.append('+')
        else:
            pass

    elif goal[0] == num_lst[-1]:
        ans.append('-')
        stack.append(num_lst.pop())
        goal.pop()

    if not num_lst:
        break

for i in ans:
    print(i)
        
        
from collections import deque

N = 5
num = deque(range(N+1)) 345
goal = deque([5,3,4])

stack = deque()
ans = []
i = 0

while True:
    
    if goal[0] != num[i]:
        if num:
            ans.append('+')
            i += 1
            if num[i] == 0:
                num.popleft()
        else:
            break

    elif goal[0] == num[i]:
        if ans[-1] == '-'
            ans.append('+')
        ans.append('-')
        stack.append(num.popleft())
        goal.popleft()

    if not num_lst and num[i] != goal[0]:
        break
    
if not goal:
    for i in ans:
        print(i)
else:
    print('NO')