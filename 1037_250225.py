# 1037 (약수)
# 32412 KB / 44 ms / 149 B 

n = int(input())
if n == 1:
    print((int(input()))**2)
else:
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[0]*nums[-1])
