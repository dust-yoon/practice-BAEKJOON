# 20233 (Bicycle)

import sys
input = sys.stdin.readline
lst = []
for _ in range(5):
    lst.append(int(input()))
if lst[4] < 30:
    print(lst[0],end=' ')
else:
    print(lst[0]+int(((lst[4]-30)*21)*lst[1]),end=' ')
if lst[4] < 45:
    print(lst[2])
else:
    print(lst[2]+int(((lst[4]-45)*21)*lst[3]))

