# 27939 (가지교배)
# 32412 KB / 1472 ms / 438 B 

N = int(input())
color = list(map(str, input().split()))
Index = []
for c in range(len(color)):
    if color[c] == 'W':
        Index.append(c+1)
        
slave, spiece = map(int, input().split())

for _ in range(slave):
    egg_plant = 'W'
    for i in list(map(int, input().split())):
        if i not in Index:
            egg_plant = 'P'
            break
    if egg_plant == 'W':
        print('W')
        exit()
print('P')