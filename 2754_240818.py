# 2754
test = input()
score = 0

a = test[0]
if a == 'A':
    score += 4.0
elif a == 'B':
    score += 3.0
elif a == 'C':
    score += 2.0
elif a == 'D':
    score += 1.0    
else:
    score = 0.0
    print(score)
    exit(0)

b = test[-1]
if b == '+':
    score += 0.3
elif b == '0':
    score += 0.0
else:
    score -= 0.3

print(score)