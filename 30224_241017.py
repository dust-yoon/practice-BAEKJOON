# 30224 (Lucky 7)

N = input()
A = '7' in N
B = not( int(N) % 7 )

if not A and not B:
    print(0)
elif not A and B:
    print(1)
elif A and not B:
    print(2)
else:
    print(3)