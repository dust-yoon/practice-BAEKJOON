# 1748 (수 이어 쓰기 1)
# 32412 KB / 36 ms / 183 B 

N = input()
l = len(N)

if l == 1:
    formul = 0
elif l == 2:
    formul = 9
else:
    formul = int(str(l-2)+'8'*(l-2)+'9')
answer = formul + (int(N)-((10)**(l-1)-1))*l
print(answer)