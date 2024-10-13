# 2108 (통계학)
# 반올림 하는 방법

import sys
input = sys.stdin.readline

N = int(input())
N_lst = []
for _ in range(N):
    N_lst.append(int(input()))

def round(x):
    x = str(x)
    if '.' in x:
        num, point = map(int, x. split('.'))
        point = str(point)[0]
        if int(point) >= 5:
            if num < 0:
                num -= 1
            else:
                num += 1
        y = num
    else:
        y = x
    return y

def fun1(lst): # 산술평균
    medium = sum(lst) / len(lst)
    return round(medium)

def fun2(lst): # 중앙값
    lst.sort()
    return lst[int(len(lst)/2)]

def fun3(lst): # 최빈값
    dic = [0]*8001
    for i in lst:
        dic[i+4000] += 1
    if dic.count(max(dic)) >= 2:
        dic[dic.index(max(dic))] = 0
    return dic.index(max(dic)) - 4000

def fun4(lst): # 범위
    return max(lst) - min(lst)

print(fun1(N_lst))
print(fun2(N_lst))
print(fun3(N_lst))
print(fun4(N_lst))


# lst = [1, 3, 8, -2, 2]
# dic = [0]*17

# for i in lst:
#     dic[i+8] += 1

# print(max(dic))
# print(dic.count((max(dic))))

# if dic.count((max(dic))) >= 2:
#     dic[dic.index(max(dic))] = 0
    
# print(dic.index(max(dic)) - 8)