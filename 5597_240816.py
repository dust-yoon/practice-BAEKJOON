# 5597
num = []
for i in range(1,31):
      num.append(i)
for j in range(28):
      num.pop(num.index(int(input())))

sorted(num)
print(num[0])
print(num[1])