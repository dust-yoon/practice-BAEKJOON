# 2751 (수 정렬하기 2)

# 1번 방법

import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

for i in range(N):
    big_index = i
    for j in range(i + 1, N):
        if lst[j] > lst[big_index]:
            big_index = j

    lst[i], lst[big_index] = lst[big_index], lst[i]

for _ in range(N):
    print(lst.pop())

# 2번 방법

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse = True)

for _ in range(N):
    print(str(lst.pop())) # 개행문자 없이 12345 출력

# 3번 방법(외부)

import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)

# 4번 방법 (외부)

num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(input()))
for i in sorted(numbers):
    print(i)
