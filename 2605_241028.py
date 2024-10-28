# 2605 (줄 세우기)

from collections import deque
N = int(input())
stack = deque(input().split())
student = deque(i+1 for i in range(N))

for i in range(N):
    k = student[i]
    student.remove(student[i])
    student.insert(i-int(stack[i]), k)

print(*student)
