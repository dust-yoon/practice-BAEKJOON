# 7510 (고급 수학)

N = int(input())
for i in range(1,N+1):
    print(f'Scenario #{i}:')
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print('yes')
        if i == N:
            break
    else:
        print('no')
        if i == N:
            break
    print()
    