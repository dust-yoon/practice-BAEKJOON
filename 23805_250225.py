# 23805 (골뱅이 찍기 - 돌아간 ㄹ)
# 32412 KB / 36 ms / 179 B 

N = int(input())

for _ in range(N):
    print('@@@'*N+' '*N+'@'*N)
for _ in range(N*3):
    print('@'*N+' '*N+'@'*N+' '*N+'@'*N)
for _ in range(N):
    print('@'*N+' '*N+'@@@'*N)