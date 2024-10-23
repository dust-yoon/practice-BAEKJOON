# 4299 (AKC 윔블던)
 
a, b = map(int, input().split())
m = a
while True:
    n = m-b
    if m+n == a:
        print(m, n)
        break
    elif n < 0:
        print(-1)
        break
    else:
        m -= 1