# 1874(스택 수열)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
n = 0
number = deque()
stack = deque(int(input()) for _ in range(N))
answer = deque()

while n < N:
    n += 1
    number.append(n)
    answer.append('+')

    if len(number):
        while number[-1] == stack[0]:
            number.pop()
            stack.popleft()
            answer.append('-')
            if not len(number):
                break
    else:
        break

if stack or number:
    print('NO')
else:
    for _ in range(len(answer)):
        print(answer.popleft())

    # print(*answer, end='\n')


# 예시 1

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(nums):
    cnt = 1
    res = []
    deq = deque()

    for num in nums:
        while 1:
            if not deq or deq[-1] < num:
                deq.append(cnt)
                cnt += 1
                res.append("+")
            elif deq[-1] == num:
                deq.pop()
                res.append("-")
                break
            else:
                return "NO"
    return res


N = int(input())
nums = [int(input()) for _ in range(N)]

res = jud(nums)
if res == "NO":
    print("NO")
else:
    print(*res, sep="\n")
        
        

# 예시 2

import sys

def main():
    n = int(sys.stdin.readline())
    numbers = list(range(n, 0, -1))  # n부터 1까지의 숫자 리스트

    stack = []  # 스택 역할을 할 리스트
    operations = []  # 연산 기록을 저장할 리스트
    stack_set = set()  # 스택에 있는 숫자를 빠르게 확인하기 위한 해시셋
    stack_list = [int(sys.stdin.readline()) for _ in range(n)]  # 입력으로 주어진 숫자 리스트

    for target in stack_list:
        # 현재 숫자가 stack에 없을 때
        while target not in stack_set:  # 스택에 목표 숫자가 없을 경우
            if numbers:  # numbers 리스트에 숫자가 남아있다면
                add_num = numbers.pop()  # 숫자를 스택에 추가
                stack.append(add_num)
                stack_set.add(add_num)  # 해시셋에 추가
                operations.append('+')  # 연산 기록에 추가
            else:
                print('NO')  # 더 이상 추가할 숫자가 없으면 불가능
                return

        # 목표 숫자가 스택의 최상단에 있을 경우
        if stack and target == stack[-1]:
            stack.pop()  # 스택에서 숫자 제거
            stack_set.remove(target)  # 해시셋에서 제거
            operations.append('-')  # 연산 기록에 추가
        # 목표 숫자가 스택에 있지만 최상단이 아닐 경우
        elif target in stack_set:
            print('NO')  # 불가능한 경우 출력
            return
        
    # 결과 출력
    print('\n'.join(operations))  # 한 번에 출력하여 성능 개선

if __name__ == '__main__':
    main()
