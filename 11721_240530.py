# letter = input('글을 입력하세요: ')
# i = len(letter.strip())
# print(i)

print("hello world")

# python BAEKJOON_11721.py
# letter = input('글을 입력하세요: ')
# i = len(letter.strip())  # 공백을 제거한 후 길이를 계산합니다.
# print(i)


# letter = input()
# string = [ letter ]
# print(str(string[0:9])\nstr(string[]))
# #format 열 함수 이용하여 정리하기




# sum = ''
# for i, letter in enumerate(letter):
#     if i%10==9:
#         sum += letter
#         print(sum)
#         sum = ''
#     else:
#         sum += letter
# if i%10!=0 and sum!='':
#     print(sum)



#     num =input()
# top=[]
# for i in num:
#     if i is not EOFError:
#         top.append(i)
#     s="".join(top)
#     if len(top) % 10 == 0:
#         print(s)
#         del top[0:10]
# print(s)


getStr = list(input())
l = len(getStr)
for a in range(l):
    if (a)%10 !=9:
        print