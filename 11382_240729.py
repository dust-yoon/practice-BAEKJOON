# 11382
numbers = input()
answer = 0
j = 0
for i in range(len(numbers)):
    if numbers[i] == " ":
        answer += int(numbers[j:i])
        j = i
answer += int(numbers[j+1:])
print(answer)
