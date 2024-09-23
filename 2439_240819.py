







    


# 1978
import sys
input = sys.stdin.readline

num = int(input())
n = list(map(int, input().split()))
# 5
# [1, 2, 3, 5, 7]
ans = 0
for i in range(num):
    if n[i] != 1:
        for j in range(2, n[i]):
            if  n[i] % j != 0:
                if j == n[i]-1:
                    ans += 1
                    print(n[i])
                continue
            else:
                break
    else:
        ans += 0
print(ans)

# 2231(생성자 구하기 어려움)
import sys
input = sys.stdin.readline

M = input()
a, b, c = 0


분해합 N 자연수 M
M = N의 생성자
분해합 256

어떤 자연수 N이 있을 때, 
그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 
경우에는 생성자가 없을 수도 있다.  = 0 출력
반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때,
N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.


216 
198

# 2292
import sys
input = sys.stdin.readline
N = int(input())
# 몇 층인지 파악하기
while True:
    [1 + [i*6 for i in range()]] < N <  [1 + [(i+1)*6 for i in range()]]
4 = 1+3  2
18 = 1+6+11  3
64 = 1 6 12 18 24 3  6