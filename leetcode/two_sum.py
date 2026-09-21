#hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # 值 → 索引
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
        return []
    
#遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""def two_sum(nums, target):
    seen = {}                          # 键：见过的数值，值：它的位置
    for i, num in enumerate(nums):
        need = target - num            # 我在找的另一个数
        if need in seen:               # 之前见过它吗？
            return [seen[need], i]     # 见过：它的位置 + 我现在的位置
        seen[num] = i                   # 没见过：把自己记下来，留给后面的数来找
    pass

print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]
print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]
print(two_sum([3, 3], 6))           # 期望 [0, 1]
"""

"""def two_sum(nums, target):
    seen={}
    for i,num in enumerate(nums):
        need = target -num
        if need in seen:
            return [seen[need],i]
        seen[num]=i

print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]
print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]
print(two_sum([3, 3], 6))           # 期望 [0, 1]



"""