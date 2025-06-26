#!/usr/bin/env python3
# Handling Program arguments
import sys
import random
# Deciding data structure
match = int(sys.argv[1])
mismatch = int(sys.argv[2])
# Variables for gap open and extension scores
gap_op = int(sys.argv[3])
gap_ex = int(sys.argv[4])
seq1 = sys.argv[5]
seq2 = sys.argv[6]
########
# print(match, mismatch, gap_op, gap_ex, seq1, seq2)
########
# ^Example ################################
        dscore = F[i-1][j-1][0]
        if nt1 == nt2:
            dscore += match
        else:
            dscore += mismatch

        lscore = F[i][j-1][0] + gap
        uscore = F[i-1][j][0] + gap

        maxscore = max(dscore, lscore, uscore)
        dirs = ''
        if maxscore == dscore:
            dirs += 'd'
        if maxscore == lscore:
            dirs += 'l'
        if maxscore == uscore:
            dirs += 'u'
        F[i][j] = [maxscore, dirs]  # yyy <- 'u' or 'l' or 'd' or 'dl' or 'du' or ... or 'dlu'

print("Optimal alignment score =", F[len(seq1)][len(seq2)][0])


# DP fill
for i in range(1, len(seq1) + 1):
    nt1 = seq1[i-1]
    for j in range(1, len(seq2) + 1):
        nt2 = seq2[j-1]

        # Matrix calculation (comparing diag)
        if nt1 == nt2:
            score_diag = F[i - 1][j - 1][0] + match
        else:
            score_diag = F[i - 1][j - 1][0] + mismatch

        # Matrix calculation (comparing up/down)
        score_up = F[i - 1][j][0] + gap
        score_left = F[i][j - 1][0] + gap

        # Storing max score
        max_score = max(score_diag, score_up, score_left)
        direction = ''
        if score_diag == max_score:
            direction += 'd'
        if score_up == max_score:
            direction += 'u'
        if score_left == max_score:
            direction += 'l'

        F[i][j] = [max_score, direction]

# Output optimal alignment score (bottom-right of the matrix)
print('Optimal alignment score =', F[len(seq1)][len(seq2)][0])

############^^^^#################
while i != 0 or j != 0:
    dirs = F[i][j][1]
    next_dir = random.choice(dirs) # next_dir = 'u' or 'l' or 'd'

    if next_dir == 'd':
        aseq1 = seq1[i-1] + aseq1
        aseq2 = seq2[j-1] + aseq2
        i -= 1
        j -= 1
    elif next_dir == 'l':
        aseq1 = '-' + aseq1
        aseq2 = seq2[j-1] + aseq2
        j -= 1
    else:
        aseq1 = seq1[i-1] + aseq1
        aseq2 = '-' + aseq2
        i -= 1
##########################################


print(aseq1)
print(aseq2)


# 지랄 빵빠레 시작
# Traceback
aseq1 = ''
aseq2 = ''

i = len(seq1)
j = len(seq2)

while i != 0 or j != 0:
    direct = F[i][j][1]
    next_dir = random.choice(direct)

    # Building sequence based on direction
    if next_dir == 'd':
        aseq1 = seq1[i - 1] + aseq1
        aseq2 = seq2[j - 1] + aseq2
        i -= 1
        j -= 1
    elif next_dir == 'l':
        aseq1 = '-' + aseq1
        aseq2 = seq2[j - 1] + aseq2
        j -= 1
    else:
        aseq1 = seq1[i - 1] + aseq1
        aseq2 = '-' + aseq2
        i -= 1

# final aligned sequences after traceback
print(aseq1)
print(aseq2)
