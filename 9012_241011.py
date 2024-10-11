# 9012 (괄호)

import sys
input = sys.stdin.readline

for _ in range(int(input())):

    sentence = input().rstrip()
    lst = []
    answer = True
    
    for i in sentence:
    
        if i == ('('):
            lst.append(1)
        elif i == ('['):
            lst.append(2)
    
        elif i == (')'):
            if not lst:
                answer = False
                break
            elif lst[-1] == 1:
                lst.pop()
            else:
                panswer = False
                break

        elif i == (']'):
            if not lst:
                answer = False
                break
            elif lst[-1] == 2:
                lst.pop()
            else:
                answer = False
                break

    if lst or not answer:
        print('NO')
        
    if not lst and answer:
        print('YES')