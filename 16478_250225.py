# 16478 (원의 분할)
# 32412 KB / 36 ms / 102 B 

a, b, c = map (int, input().split())
d = a*c/b
if d.is_integer():
    print(int(d))
else:
    print(d)