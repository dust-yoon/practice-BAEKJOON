# 2729(수정필요)
import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    A, B = map(str, input().split())

    A_plus = 0
    B_plus = 0
    n = 0
    for i in range(len(A)):
        A_plus += (2**(len(A)-(i+1)))*int(A[i])
    for i in range(len(B)):
        B_plus += (2**(len(B)-(i+1)))*int(B[i])
    plus = A_plus + B_plus
    for j in range(81):
        if 2**j < plus < 2**(j+1):
            n = j
            break

    ans = [1]
    for k in range(n):
        if plus - 2**(n-k) > 2**(n-k-1):
            ans.append(1)
        else:
            ans.append(0)

    ans = map(str, ans)
    print(''.join(ans))

    3
1001101 10010
1001001 11001
1000111 1010110
 
1011111
1100010
10011101