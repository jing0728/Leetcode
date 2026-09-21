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