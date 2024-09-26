# 2675
import sys
input = sys.stdin.readline
testcase = int(input())

for i in range(testcase):
    test = []
    time, word = input().split()
    time = int(time)
    for j in range(len(word)):
        test.append(word[j]*time)
    print(''.join(test))