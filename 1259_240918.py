# 1259 (팰린드롬수)

import sys
input = sys.stdin.readline

A = True

while A:
    num = input().strip()
    L = len(num)

    if int(num) == 0:
        A = False
    
    if L == 1 and int(num) != 0:
        print('yes')

    for i in range(L//2):
        
        if num[i] == num[-(i+1)]:
            if i == (L//2)-1:
                print('yes')
                break
            continue
        
        else:
            print('no')
            break
        

# A = True

# while A:
#     num = input()
#     B = False
#     if num == 0:
#         A = False

#     for i in range(1, (len(num)//2)+1):#121(0 1(-2) -1) 0 1
#         if num[i] != num[-(i+1)]:
#             A = False
#         if i == num[len(num)//2]:
#             B = True
#             A = False

#     if B:
#         print('yes')
#     else:
#         print('no')
