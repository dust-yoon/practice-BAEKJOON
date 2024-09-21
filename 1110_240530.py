
# if num < 10:
#     print(str(0) + str(num))

# num = int(input("무작위 수를 입력하세요: "))
# num1 = num // 10
# num2 = num % 10
# print("입력하신 값은: " , str(num1)+str(num2))
# print("각자리의 숫자를 더한 값은: ", num1 + num2)
# num3 = (num1 + num2) % 10
# print("새로운 수: ", str(num2)+str(num3))

number = int(input())
first = number
count = 0
while True:
    num1 = number // 10 # 10보다 작으면 앞에 0이 들어감
    num2 = number % 10
    num3 = (num1 + num2) % 10 # 각 자리의 숫자를 더함, 그 수의 오른쪽 자리수 = num3
    number = (num2*10) + num3 # 새로운 수 생성
    count +=1
    if( first == number):
        break
print(count)
 
# print(count)


# import random

# a = int(input("Generate random numbers:"))
# randlist = []
# for _ in range(a):
#     input("엔터를 눌러 무작위 수를 입력하세요")
#     random_number = random.randint(1,10000)
#     randlist.append(random_number)
#     print(random_number)
# print("\n랜덤 수의 합:", sum(randlist))

# print(sum(list(map(int,input().split()))))