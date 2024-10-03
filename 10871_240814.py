# 10871

# import sys
# map 사용
# join() 함수 이용

import sys
length, N = map(int, input().split())
ans = []
number = list(map(int, sys.stdin.readline().split()))

for i in range(length):
    if number[i] < N:
        ans.append(number[i])

print(' '.join(map(str, ans)))



N, X = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(N):
if(num_list[i] < X):
print(num_list[i] , end = ' ')




x,y = map(int,input().split())
n = list(map(int,input().split()))
a = []
for i in n:
    if i<y:
        a.append(i)
for i in a:
    print(i,end=" ")