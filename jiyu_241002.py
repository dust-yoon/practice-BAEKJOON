file = open('jiyoon.txt', 'a', encoding = 'utf-8')
file.write('안녕')

file = open('jiyoon.txt', 'r', encoding = 'utf-8', errors = "ignore")
str = file.read()

print(f'{str}은 jiyoon.txt의 내용입니다.')

file.close()

with open('jiyoon.txt', 'a') as f:
    f.write('python')
    
with open('jiyoon.txt', 'r', errors = "ignore") as f:
    print(f.read())