# 1009 (분산처리)

# 1. 테스트 케이스 받기 n 받고 반복
# 2. a^^b 꼴 값을 나눠야함... 근데 이걸 왜알려줌
# 나누기 10... 나머지 값을 알아얒

#     # 걍 끝자리만 알려주면 되는거 아님?
#     1 1
#     2 4 8 6...
#     3 9 7 1..
#     4 6
#     5 ...
#     6...
#     7 9 3 1
#     8 4 2 6
#     9 1
#     0 0 

import sys
input = sys.stdin.readline

N = int(input())

lst = [[0]*4,
    [1]*4,
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6]*2,
    [5]*4,
    [6]*4,
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1]*2
    ]

for i in range(N):
    a, b = map(str, input().split())
    A = int(a[-1])
    B = (int(b)-1) % 4
    if A == 0:
        print(10)
    else:
        print(lst[A][B])

# 다른 예시
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    last_digit = pow(a, b, 10)  # (a^b) % 10
    
    if last_digit == 0:
        print(10)
    else:
        print(last_digit)