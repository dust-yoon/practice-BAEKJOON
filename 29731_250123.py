# 29731 (2033년 밈 투표)

original = ['Never gonna give you up'
          ,'Never gonna let you down'
          ,'Never gonna run around and desert you'
          ,'Never gonna make you cry'
          ,'Never gonna say goodbye'
          ,'Never gonna tell a lie and hurt you'
          ,'Never gonna stop']
N = int(input())
ans = False
for i in range(N):
    sentence = input()
    if sentence in original:
        continue
    else:
        ans = True
if ans:
    print('Yes')
else:
    print('No')