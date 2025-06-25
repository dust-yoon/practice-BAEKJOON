# 19592 (장난감 경주)
#  KB /  ms /  B 

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, x, y = map(int, input().split())
    v_list = list(map(int, input().split()))
    v_max = max(v_list[:-1])
    v_mine = v_list[-1]
    buster = 0
    
    if x/v_max <= x/v_mine:
        buster = v_mine
        while x/v_max <= (x-buster)/v_mine + 1:
            buster += 1
            if buster == y:
                buster = -1
                break
            
    print(buster)
    
import sys
input = sys.stdin.readline

def min_buster(n, x, y, v_list):
    v_max = max(v_list[:-1])  # 마지막을 제외한 최대 속도
    v_mine = v_list[-1]       # 내 자동차 속도
    
    if v_mine >= v_max:
        return 0  # 이미 가장 빠른 경우 부스터 필요 없음

    left, right = 1, y
    result = -1

    while left <= right:
        mid = (left + right) // 2
        new_time = (x - mid) / v_mine + 1  # 부스터 사용 후 시간
        old_time = x / v_max  # 기존 시간

        if new_time < old_time:  # 부스터 사용이 효과가 있는 경우
            result = mid
            right = mid - 1  # 더 작은 부스터 값 찾기
        else:
            left = mid + 1  # 더 큰 부스터 값 필요
    
    return result

T = int(input())
for _ in range(T):
    n, x, y = map(int, input().split())
    v_list = list(map(int, input().split()))
    print(min_buster(n, x, y, v_list))

# 이진 탐색 활용(O(log y)) → 실행 속도 개선
# 불필요한 연산 제거
# 가독성 향상 → min_buster() 함수로 로직 분리
# 1. 불필요한 연산 제거: x/v_max <= x/v_mine 조건은 필요하지 않으며, v_max와 v_mine을 비교하여 판단하는 것이 더 명확합니다.
# 2. 이진 탐색 적용: buster를 1부터 y까지 증가시키는 대신, 이진 탐색을 활용하여 더 빠르게 값을 찾도록 개선했습니다.
# 3. 시간 복잡도 감소: 기존 코드는 buster를 선형 탐색하여 최대 y번 반복했지만, 이진 탐색을 적용하여 O(log y)로 줄였습니다.