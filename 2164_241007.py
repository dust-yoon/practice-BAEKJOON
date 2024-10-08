# 2164 (카드 2)
    # 51028KB 188ms	252B
    
# N = int(sys.stdin.readline())
# N_lst = list(range(1, N+1))[::-1]

    # 처음부터 deq 함수로 해결해도 되는 문제
        # while len(N_lst) > 1:
        #     N_lst.pop()
        #     deque.extendleft(deque(N_lst))
            
        # print(*N_lst)


import sys
from collections import deque

N = int(sys.stdin.readline().strip())
deq = deque(range(1, N+1))

if N == 1:
   print(N)
   exit()

while len(deq) > 1:
    deq.popleft() # 가장 왼쪽 삭제
    deq.append(deq.popleft())

print(deq[0])
    


# pop()의 시간 복잡도는 O(n)이므로 더 좋은 방법이 있을 것
# python deque, popleft() 에 대해 조사 필요

# deque(from collections import deque / deq = deque())
    # deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
    # deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
    # deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
    # deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
    # deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
    # deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
    # deque.remove(item): item을 데크에서 찾아 삭제한다.
    # deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).