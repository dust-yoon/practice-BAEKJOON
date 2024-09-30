# 1676 (팩토리얼 0의 개수)

N = int(input())
factorial = 1

for i in range(1, N+1):
    factorial *= i

time = 0
N = list(str(factorial))
# N = list(map(int, str(N).split('')))

while True:
    last = N.pop()
    if last == "0":
        time += 1
    elif last != "0":
        print(time)
        break