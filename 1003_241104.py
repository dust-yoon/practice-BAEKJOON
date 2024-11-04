# 1003 (피보나치 함수)

# 1. 내가 풀이한 함수 (메모리 초과 출력)

def fibonacci(N):
    if N == 1:
        return 1
    elif not N:
        return 0
    else:
        return fibonacci(N-1), fibonacci(N-2)

for _ in range(int(input())):
    dic = {0: 0, 1: 0}
    result = str(fibonacci(int(input()))).replace('(', '').replace(')', '')

    for i in result:
        if i.isdigit():
            dic[int(i)] += 1
        else:
            pass

    print(dic[0], dic[1])

# 2. 기타 내용 참조 - 이건 또 시간초과임
def fibonacci(N):

    if N == 1:
        return {1: 1, 0: 0}
    elif N == 0:
        return {1: 0, 0: 1}

    fibo_1 = fibonacci(N - 1)
    fibo_2 = fibonacci(N - 2)

    return {
        1: fibo_1[1] + fibo_2[1],
        0: fibo_1[0] + fibo_2[0]
    }

for _ in range(int(input())):
    result = fibonacci(int(input()))
    print(result[0], result[1])

# 3. 이미 게산된 결과를 저장해두는 메모이제이션 활용해야 함
# {메모리: 34040KB / 시간: 64ms / 코드 길이: 450B}

from functools import lru_cache

@lru_cache(None) # 캐시 크기를 제한하지 않는 설정
def fibonacci(N):

    if N == 1:
        return {1: 1, 0: 0}
    elif N == 0:
        return {1: 0, 0: 1}

    fibo_1 = fibonacci(N - 1)
    fibo_2 = fibonacci(N - 2)

    return {
        1: fibo_1[1] + fibo_2[1],
        0: fibo_1[0] + fibo_2[0]
    }

for _ in range(int(input())):
    result = fibonacci(int(input()))
    print(result[0], result[1])

# 4. 아니면 아예 재귀함수를 계속해서 사용하지 않고 반복문만을 사용하는 것도 괜춘
# {메모리: 31120KB / 시간: 40ms / 코드 길이: 559B}

def fibonacci(N):
    # 초기값 설정: N이 0일 때와 1일 때의 호출 횟수
    count = [(1, 0), (0, 1)]  # (0의 호출 횟수, 1의 호출 횟수)
    
    # 필요한 만큼 count 배열을 채워 넣습니다.
    for i in range(2, N + 1):
        count_0 = count[i - 1][0] + count[i - 2][0]
        count_1 = count[i - 1][1] + count[i - 2][1]
        count.append((count_0, count_1))
    
    return count[N]

# 여러 테스트 케이스 실행
for _ in range(int(input())):
    result = fibonacci(int(input()))
    print(result[0], result[1])
