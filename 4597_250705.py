# 4597 (패리티)

while True:
    string = list(input())
    num = string.count('1')
    if string[-1] == 'e':
        string.pop()
        if num%2 == 1:
            string.append('1')
        else:
            string.append('0')
    elif string[-1] == 'o':
        string.pop()
        if num%2 == 1:
            string.append('0')
        else:
            string.append('1')
    else:
        break
    for i in string:
        print(i,end='')
    print()