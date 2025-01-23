# 2579 (계단 오르기)

def miss():
    import sys
    input = sys.stdin.readline

    N = int(input())
    lst = []
    for i in range(N):
        new = []
        new.append(int(input()))
        new.append(i+1)
        lst.append(new)

    total = lst[N-1][0]
    lst.pop()
    lst.sort(reverse=True)
    stack = set([N])

    for a in lst:
        index = int(a[1])
        number = int(a[0])
        if index+1 in stack:
            if not index-1 in stack and not index+2 in stack:
                total += number
                stack.add(index)
            else:
                continue
        elif index-1 in stack:
            if not index-2 in stack and not index+1 in stack:
                total += number
                stack.add(index)
            else:
                continue
        else:
            total += number
            stack.add(index)

    print(total)

import sys
input = sys.stdin.readline
#입력
N = int(input())
nums = []
exist = []

if N >= 3:
    for n in range(N-1):
        num = int(input())
        nums.append(num)
        exist.append(0)
        if n == N-2:
            if nums[n]>nums[n-1]:
                exist[n] = 1
            else:
                exist[n-1] = 1
    nums.append(int(input()))
    exist.append(1)
    numss=nums.copy()
    numss[N-3:]=0,0,0
    
    while numss != [0]*N:
        key = numss.index(max(numss[:-3]))
        numss[key]=0
            
        if not exist[key] : # exsit[key] == 0
            
            if key == 0 and not (exist[key+1] and exist[key+2]):
                exist[key] = 1
            elif key == 1:
                if not (exist[key+1] and exist[key+2]) and not(exist[key-1] and exist[key+1]):
                    exist[key] = 1
            
            else:
                if not(exist[key-1] or exist[key+1]): # _000_
                    exist[key] = 1
                elif exist[key+1]: # __01_
                    if not (exist[key-1] or exist[key+2]): #_0010 
                        exist[key] = 1
                elif exist[key-1]: # _10__
                    if not (exist[key+1] or exist[key-2]): # 0100_
                        exist[key] = 1
                else: # 그 외 1이 들어갈 수 없는 자리
                    continue
                
        else: # exist[key] != 0
            continue
    
    total = 0
    for n in range(N):
        if exist[n] == 1:
            total += nums[n]
    
else:
    nums = [int(input()) for x in range(N)]
    total = sum(nums)
    
print(total)
print(exist)

# DP 사용 방식 이용
import sys
input = sys.stdin.readline

# 입력
N = int(input())
stairs = [int(input()) for _ in range(N)]

# DP 배열 초기화
if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    dp = [0] * N
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[-1])
