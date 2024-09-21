# 1330
numbers = input()
space = numbers.index(" ")
a = int(numbers[:space])
b = int(numbers[space+1:])
if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")