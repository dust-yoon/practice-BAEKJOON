# 5300 (Fill the Rowboats!)

N = int(input())
X = 1
while True:
    print(X, end=' ')
    if not X % 6 and X != N:
        print('Go!', end=' ')
    if not X % 6 and X == N:
        print('Go!')
    if X == N:
        break
    X += 1
if X % 6:
    print('Go!')