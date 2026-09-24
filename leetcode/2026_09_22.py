"""def reverse_string(s):
    s[:]=s[::-1]
    return s


s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

"""def reverse_string(s):
    new=[]
    le=len(s)
    for i,ch in enumerate(s):
        new.append(s[le-1-i])
    s[:]=new
    return s



s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

"""def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

"""def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[right],s[left]=s[left],s[right]
        right-=1
        left+=1

s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

"""def two_sum_sorted(numbers, target):
    left=0
    right=len(numbers)-1
    while left<right:
        total = numbers[left]+numbers[right]
        if total==target:
            return [left+1,right+1]
        elif total>target:
            right-=1
        else:
            left+=1
            


print(two_sum_sorted([2, 7, 11, 15], 9))
# 期望 [1, 2]

print(two_sum_sorted([2, 3, 4], 6))
# 期望 [1, 3]

print(two_sum_sorted([-1, 0], -1))
# 期望 [1, 2]"""

"""def move_zeroes(nums):
    left=0
    while left<(len(nums)-1):
        if nums[left]==0:
            nums.pop(left)
            nums.append(0)
        left+=1
    return nums



nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)
# 期望 [1, 3, 12, 0, 0]

nums2 = [0]
move_zeroes(nums2)
print(nums2)
# 期望 [0]

nums3 = [1, 0, 2, 0, 3]
move_zeroes(nums3)
print(nums3)
# 期望 [1, 2, 3, 0, 0]"""

"""def move_zeroes(nums):
    left=0
    for right in range(len(nums)):
        if nums[right] !=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums

nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)
# 期望 [1, 3, 12, 0, 0]

nums2 = [0]
move_zeroes(nums2)
print(nums2)
# 期望 [0]

nums3 = [1, 0, 2, 0, 3]
move_zeroes(nums3)
print(nums3)
# 期望 [1, 2, 3, 0, 0]"""

def sorted_squares(nums):
    left=0
    for right in range(len(nums)):
        if abs(nums[right])<abs(nums[left]):
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums


print(sorted_squares([-4, -1, 0, 3, 10]))
# 期望 [0, 1, 9, 16, 100]

print(sorted_squares([-7, -3, 2, 3, 11]))
# 期望 [4, 9, 9, 49, 121]

print(sorted_squares([0]))
# 期望 [0]