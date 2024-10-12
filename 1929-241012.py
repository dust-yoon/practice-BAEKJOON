# 1929 (소수 구하기)

import math

M, N = map(int, input().split())
stack = set(range(M, N+1))
if 1 in stack:
    stack.discard(1)
# 에라토스테네스의 체 적용 (N의 제곱근까지만 검사)
limit = int(math.sqrt(N)) + 1
is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, limit):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
            
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
        
# k = 2
# if N == 1 or N == 2:
#     print(*stack)
#     exit()
# while k != limit:
#     for i in range(2, int(N/k)+1):
#         stack.discard(k*i)
#     k += 1
# for j in stack:
#     print(j)