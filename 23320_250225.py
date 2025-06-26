# 23320 (홍익 절대평가)
# 32412 KB / 36 ms / 259 B 

num = int(input())
score = list(map(int, input().split()))
score.sort()

A_ratio, min_score = map(int, input().split())
A_num = (num * A_ratio)//100

nums = 0
for s in score:
    if s >= min_score:
        break
    nums += 1
    
print(f'{A_num} {num-nums}')

# sys.stdin.readline 의 문제였음 => strip()