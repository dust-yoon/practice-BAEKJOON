# 31775 (글로벌 포닉스)

K = True
for _ in range(3):
    sentence = input()
    if not (sentence[0] == 'k' or sentence[0] == 'l' or sentence[0] == 'p'):
        K = False
if K:
    print('GLOBAL')
else:
    print('PONIX')