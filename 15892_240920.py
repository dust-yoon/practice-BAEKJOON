# 15892 (Hashing)

import sys
input = sys.stdin.readline

L = int(input())
sentence = input().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = []
mod = 10 ** 9 + 9
answer = 0

# for i in range(L):
#     num.append(alpha.index(sentence[i])+1)

# for j in range(L):
#     answer = (answer + (num[j] * (31**j))) % mod

for j in range(L):
    num = alpha.index(sentence[j]) + 1
    answer = (answer + num * pow(31, j, mod)) % mod

print(answer)