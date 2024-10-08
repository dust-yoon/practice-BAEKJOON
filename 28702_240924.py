# 28702 (FizzBuzz)

for i in range(3):
    word = input()
    if word.isdigit():
        num = int(word)
        number = num + (3-i)
    else:
        continue

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0 and number % 5 != 0:
    print('Fizz')
elif number % 3 != 0 and number % 5 == 0:
    print('Buzz')
else:
    print(number)