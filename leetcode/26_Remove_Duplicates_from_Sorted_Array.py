def remove_duplicates(nums):
    left=1
    for right in range(len(nums)):
        if nums[right]!=nums[right-1]:
            nums[left]=nums[right]
            left+=1
    return left


nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print(k1)
print(nums1[:k1])
# 期望：
# 2
# [1, 2]

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = remove_duplicates(nums2)
print(k2)
print(nums2[:k2])
# 期望：
# 5
# [0, 1, 2, 3, 4]