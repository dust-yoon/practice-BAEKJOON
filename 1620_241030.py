# 1620 (나는야 포켓몬 마스터 이다솜)

# 튜플 자료형 https://blockdmask.tistory.com/447
# 자료형 시간복잡도 https://velog.io/@oum/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%B0%EC%82%B0-%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84

# 숫 -> 영 (O(1)) 선형탐색(O(N))이 시간 초과를 유발함
# 시간 관리 중요함

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
dic_n = {}

for i in range(1,N+1):
    word = input().strip()
    dic[word] = i
    dic_n[i] = word

for _ in range(M):
    word_que = input().strip()
    if word_que.isalpha():
        print(dic[word_que])
    else:
        print(dic_n[int(word_que)])
