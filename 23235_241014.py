# 23235 (The Fastest Sorting Algorithm In The World)

n = 1
while True:    
    lst = list(input().split())
    if lst == ['0']:
        break
    print(f'Case {n}: Sorting...', end=' ')
    lst.sort()
    print('done!')
    n += 1
