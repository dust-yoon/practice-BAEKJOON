# 2839 (설탕 배달)

N = int(input())

five = N // 5 

while five >= 0:
    total = N
    total -= (5 * five)

    if total:

        if not total % 3:
            print(five + (total // 3))
            exit()
        else:
            five -= 1

        continue
    
    else:
        print(five)
        exit()

print(-1)