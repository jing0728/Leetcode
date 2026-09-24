def three_sum(nums):
    nums.sort()
    ans=set()
    for i in range(len(nums)):
        left=i+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                ans.add((nums[i],nums[left],nums[right]))
                left+=1
                right-=1
    return  [list(x) for x in ans]


print(three_sum([-1, 0, 1, 2, -1, -4]))
# 期望 [[-1, -1, 2], [-1, 0, 1]]

print(three_sum([0, 1, 1]))
# 期望 []

print(three_sum([0, 0, 0]))
# 期望 [[0, 0, 0]]