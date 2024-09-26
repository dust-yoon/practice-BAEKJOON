# 1181 (단어 정렬)

import sys
input = sys.stdin.readline

# 정렬 def
def list_len(word):
    if len(word) <= 1:
        return word
    else:
        pivot = word[0]
        less = [x for x in word[1:] if len(x) <= len(pivot)]
        greater = [x for x in word[1:] if len(x) > len(pivot)]

        return list_len(less) + [pivot] + list_len(greater)
# 중복 제거 및 정렬 적용
def sort_word(word):
    word = list(set(word))
    sorted_word = list_len(word)
    return sorted_word

N = int(input())
word = [input().strip() for _ in range(N)]

# 한 줄 for 문으로 해결하기
# for _ in range(N):
#     lst.append(input().strip())

sorted_word = sort_word(word)
for word in sorted_word:
    print(word)

import sys
input = sys.stdin.readline

def sort_word(word):
    word = list(set(word))
    sorted_word = sorted(word, key=lambda x: (len(x), x))
    return sorted_word

N = int(input())
word = [input().strip() for _ in range(N)]

sorted_word = sort_word(word)

for w in sorted_word:
    print(w)
