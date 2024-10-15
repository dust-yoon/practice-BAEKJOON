# 16204 (카드 뽑기)

N, M, K = map(int, input().split())
total = min(M, K)
total += min(N-M, N-K)

print(total)