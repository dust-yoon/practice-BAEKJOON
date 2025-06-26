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
# Creating DP matrix
M = {}
IX = {}
IY = {}
for i in range(len(seq1) + 1):
    M[i] = {}
    IX[i] = {}
    IY[i] = {}
# Initialization for M, IX, IY
M[0][0] = [0, '']
IX[0][0] = [0, '']
IY[0][0] = [0, '']
# Column initialization for M, IX, IY
for i in range(1, len(seq1) + 1):
    M[i][0] = [float('-inf'), '']
    IX[i][0] = [gap_op + (i-1)*(gap_ex), 'u']
    IY[i][0] = [float('-inf'), '']
    IY[i][1] = [float('-inf'), '']
# Row initialization for M, IX, IY
for j in range(1, len(seq2) + 1):
    M[0][j] = [float('-inf'), '']
    IX[0][j] = [float('-inf'), '']
    IX[1][j] = [float('-inf'), '']
    IY[0][j] = [gap_op + (j-1)*(gap_ex), 'l']

# DP fill
for i in range(1, len(seq1) + 1):
    nt1 = seq1[i-1]
    for j in range(1, len(seq2) + 1):
        nt2 = seq2[j-1]
        ## For M
        # Code for finding the max score for M
        if j not in M[i]:
            direction = ''
            max_score = max(M[i-1][j-1][0], IX[i-1][j-1][0], IY[i-1][j-1][0])
            # Direction for the max score
            if M[i-1][j-1][0] == max_score:
                direction += 'd'
            if IX[i-1][j-1][0] == max_score:
                direction += 'u'
            if IY[i-1][j-1][0] == max_score:
                direction += 'l'
            # Make max score
            if nt1 == nt2:
                max_score += match
            else:
                max_score += mismatch
            # Insert score & directions
            M[i][j] = [max_score, direction]

        ## For IX
        # Code for finding the max score for IX
        if j not in IX[i]:
            direction = ''
            max_score = max(M[i-1][j][0] + gap_op, IX[i-1][j][0] + gap_ex)
            # Direction for the max score
            if M[i-1][j][0] + gap_op == max_score:
                direction += 'd'
            if IX[i-1][j][0]+ gap_ex == max_score:
                direction += 'u'
            # Insert score & directions
            IX[i][j] = [max_score, direction]

        ## For IY
        # Code for finding the max score for IY
        if j not in IY[i]:
            direction = ''
            max_score = max(M[i][j-1][0] + gap_op, IY[i][j-1][0] + gap_ex)
            # Direction for the max score
            if M[i][j-1][0] + gap_op == max_score:
                direction += 'd'
            if IY[i][j-1][0] + gap_ex == max_score:
                direction += 'l'
            # Insert score & directions
            IY[i][j] = [max_score, direction]
# Finding the max score from M, IX, IY
final_max_score = max(M[len(seq1)][len(seq2)][0], IX[len(seq1)][len(seq2)][0], IY[len(seq1)][len(seq2)][0])
print("Optimal alignment score =", final_max_score)

# Track back
aseq1 = ''
aseq2 = ''
i = len(seq1)   # 5
j = len(seq2)   # 4
# Code for finding the starting matrix among M, IX, IY
# Need to perform random selection
dirs_start = ''
if final_max_score == M[i][j][0]:
    dirs_start += 'm'
if final_max_score == IX[i][j][0]:
    dirs_start += 'x'
if final_max_score == IY[i][j][0]:
    dirs_start += 'y'
# Select one direction
dir_s = random.choice(dirs_start)
if dir_s == 'm':
    matrix = M
elif dir_s == 'x':
    matrix = IX
else:
    matrix = IY

while i != 0 or j != 0:
    # Need to find the current location (M, IX, or IY)
    # Need to get the directions from the current matrix
    dirs_next = matrix[i][j][1]
    dir_n = random.choice(dirs_next)
    
    if matrix == M:
        aseq1 = seq1[i-1] + aseq1
        aseq2 = seq2[j-1] + aseq2
        i -= 1
        j -= 1
    elif matrix == IX:
        aseq1 = seq1[i-1] + aseq1
        aseq2 = '-' + aseq2
        i -= 1
    else:
        aseq1 = '-' + aseq1
        aseq2 = seq2[j-1] + aseq2
        j -= 1
        
    if dir_n == 'd':
        matrix = M
    elif dir_n == 'u':
        matrix = IX
    else:
        matrix = IY
    # Code for handling directions: M(d, IX, IY), IX(M, u), IY(M, l)
# final aligned sequences after traceback
print(aseq1)
print(aseq2)



print('=====< M Matrix >=====')
for i in M:
    for j in M[i]:
        k = M[i][j][0]
        if M[i][j][0] == float('-inf'):
            k = 'x'
        k = str(k)
        if len(k) != 2:
            k = ' ' + k
        print(k, end=' ')
    print()
print('=====< IX Matrix >=====')
for i in IX:
    for j in IX[i]:
        k = IX[i][j][0]
        if IX[i][j][0] == float('-inf'):
            k = 'x'
        k = str(k)
        if len(k) != 2:
            k = ' ' + k
        print(k, end=' ')
    print()
print('=====< IY Matrix >=====')
for i in IY:
    for j in IY[i]:
        k = IY[i][j][0]
        if IY[i][j][0] == float('-inf'):
            k = 'x'
        k = str(k)
        if len(k) != 2:
            k = ' '+k
        print(k, end=' ')
    print()
