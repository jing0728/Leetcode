# def contains_nearby_duplicate(nums, k):
#     cout={}
#     for i,num in enumerate(nums):
#         if num in cout:
#             if abs(cout[num]-i)<=k:
#                 return True
#         cout[num]=i
#     return False



# print(contains_nearby_duplicate([1, 2, 3, 1], 3))
# # 期望 True

# print(contains_nearby_duplicate([1, 0, 1, 1], 1))
# # 期望 True

# print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
# # 期望 False

# print(contains_nearby_duplicate([1, 2, 3, 1], 2))
# # 期望 False

# print(contains_nearby_duplicate([], 0))
# # 期望 False

# def is_happy(n):
#     same=set()
#     while n!=1:
#         if n in same:
#             return False
#         same.add(n)
#         total=0
#         for i in str(n):
#             total+=int(i)**2
#         n=total
#     return True


# print(is_happy(19))
# # 期望 True

# print(is_happy(2))
# # 期望 False

# print(is_happy(1))
# # 期望 True

# print(is_happy(7))
# # 期望 True


# def is_palindrome(s):
#     word=''.join(filter(str.isalnum,s)).lower()
#     return word==word[::-1]


# print(is_palindrome("A man, a plan, a canal: Panama"))
# # 期望 True

# print(is_palindrome("race a car"))
# # 期望 False

# print(is_palindrome(" "))
# # 期望 True

# print(is_palindrome("0P"))
# # 期望 False

# def sorted_squares(nums):
#     ans = [0] * len(nums)

#     left = 0
#     right = len(nums) - 1
#     pos = len(nums) - 1

#     while left <= right:
#         if abs(nums[left]) > abs(nums[right]):
#             ans[pos]=nums[left]**2
#             left+=1
#         else:
#             ans[pos]=nums[right]**2
#             right-=1

#         pos -= 1

#     return ans
        

# print(sorted_squares([-4, -1, 0, 3, 10]))
# # 期望 [0, 1, 9, 16, 100]

# print(sorted_squares([-7, -3, 2, 3, 11]))
# # 期望 [4, 9, 9, 49, 121]

# print(sorted_squares([0]))
# # 期望 [0]

# print(sorted_squares([-5, -3, -2, -1]))
# # 期望 [1, 4, 9, 25]

# def max_area(height):
#     left=0
#     right=len(height)-1
#     ans=[]
#     while left<right:
#         area = min(height[left], height[right]) * (right - left)
#         ans.append(area)
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max(ans)

# print(max_area([1,8,6,2,5,4,8,3,7]))
# # 期望 49

# print(max_area([1,1]))
# # 期望 1

# print(max_area([4,3,2,1,4]))
# # 期望 16

# print(max_area([1,2,1]))
# # 期望 2

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