# 10809
S = input()
ans = []
alpha = ['a', 'b', 'c', 'd'
        , 'e', 'f', 'g', 'h'
        , 'i', 'j', 'k', 'l'
        , 'm', 'n', 'o', 'p'
        , 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(26):
    ans.append(str(S.find(alpha[i])))
print(*ans)      