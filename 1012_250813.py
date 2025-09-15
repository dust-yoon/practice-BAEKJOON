# 1012 (유기농 배추)

import sys
input = sys.stdin.readline

T = int(input())
# Devide test case
for _ in range(T):
    # INPUT
    M,N,K = map(int, input().split())
    # Make a check board
    board = []
    for i in range(M):
        board.append([])
    # Fill board
    for _ in range(K):
        m,n = map(int, input().split())
        board[m].append(n)
    
    # OUTPUT
    #비어있으면 삭제 후 새로운 애 데려와야해
    for j in range(len(board)):
        if board[j] == False:
            board.remove(j)
    
        