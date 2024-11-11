# 2606 (바이러스)

# 7대
# 네트워크 상 직접 연결되어있는 컴퓨터 쌍의 수
# 6
#
#   1
# 2 - 5
# 3   6
#
# 4 - 7
#
# 딕셔너리
# 1:2 2:3 1:5 이런식으로 연결
# 개수 변수 생성
# 있는지 없는지 확인
# def 로 이어지게 해보자 재귀함수로
# 있으면 삭제, 삭제했으면 한번 더 돌려보기(중복 방지)
# 만들면서 += 실행하기

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dic = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = list(b)

time = set([1])
def virus(N):
    time.add(N)
    if dic[N]:
        return virus(dic[N].pop())
    elif not dic[N]:
        dic[N].pop()

print(len(time))

dic = {3:[1,2],5:3}
dic[6] = [1]
print(dic)
dic[6].append(7)
print(dic)
dic[6].pop()
print(dic)
dic[6].pop()
print(dic)
if not dic[6]:
  dic.pop(6)
print(dic)
