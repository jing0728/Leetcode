def contains_nearby_duplicate(nums, k):
    count={}
    for i,num in enumerate(nums):
        if num in count and abs(count[num]-i)<=k:
            return True
        else:
            count[num]=i
    return False

print(contains_nearby_duplicate([1, 2, 3, 1], 3))
# 期望 True

print(contains_nearby_duplicate([1, 0, 1, 1], 1))
# 期望 True

print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
# 期望 False

print(contains_nearby_duplicate([1, 2, 3, 1], 2))
# 期望 False

print(contains_nearby_duplicate([], 0))
# 期望 False