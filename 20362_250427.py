# 20362 (유니대전 퀴즈쇼)
# 32544 KB / 40 ms / 319 B 

import sys
input = sys.stdin.readline

n, ans_name = input().split()
data = {}

for _ in range(int(n)):
    name, chat = input().split()
    if name != ans_name:
        data[chat] = data.get(chat, 0) + 1
    else:
        ans_chat = chat
        break

if ans_chat in data:
    print(data[ans_chat])
else:
    print(0)

# N, ans_chat = input().split()
# N = int(N)

# wro_chat_num = 0
# for _ in range(N):
#     chat, temp = input().split()
#     if chat != ans_chat:
#         wro_chat_num += 1
#     else:
#         break

# print(wro_chat_num)