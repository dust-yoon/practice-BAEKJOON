# 4949 (균형잡힌 세상)

import sys
input = sys.stdin.readline

while True:

    sentence = input().rstrip()
    if sentence == '.':
        exit()
    
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

        else:
            continue

    if lst or not answer:
        print('no')
        
    if not lst and answer:
        print('yes')