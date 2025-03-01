# 1547 (공)

M = int(input())
cup = [x+1 for x in range(3)]
for i in range(M):
    cup1, cup2 = map(int, input().split())
    # cup[cup.index(cup2)],cup[cup.index(cup1)]=cup[cup.index(cup1)],cup[cup.index(cup2)]
    a = cup.index(cup1)
    b = cup.index(cup2)
    cup[a],cup[b] = cup[b],cup[a]
print(cup[0])