# 2579 (계단 오르기)

import sys
input = sys.stdin.readline
 
N = int(input())
lst = []
for i in range(N):
    new = []
    new.append(int(input()))
    new.append(i+1)
    lst.append(new)

total = lst[N-1][0]
lst.pop()
lst.sort(reverse=True)
stack = set([N])

for a in lst:
    index = int(a[1])
    number = int(a[0])
    if index+1 in stack:
        if not index-1 in stack and not index+2 in stack:
            total += number
            stack.add(index)
        else:
            continue
    elif index-1 in stack:
        if not index-2 in stack and not index+1 in stack:
            total += number
            stack.add(index)
        else:
            continue
    else:
        total += number
        stack.add(index)

print(total)