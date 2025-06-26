# 28113 (정보섬의 대중교통)

N,A,B = map(int, input().split())
if A > B:
    print('Subway')
elif A < B:
    print('Bus')
else:
    print('Anything')