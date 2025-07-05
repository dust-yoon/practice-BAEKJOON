# 14626 (ISBN)

# Make num_lst
num_lst = []
L = input()
for i in range(len(L)):
    if i%2 == 0:
        num_lst.append([1,L[i]])
    else:
        num_lst.append([3,L[i]])
num = L.find('*')

# devide two calculation
total = 0
for A,B in num_lst[0:num]:
    total += A * int(B)
for A,B in num_lst[num+1:]:
    total += A * int(B)

last_num = (10-total%10)%10

for x in range(10):
    if (total + num_lst[num][0] * x) % 10 == 0:
        print(x)
        break