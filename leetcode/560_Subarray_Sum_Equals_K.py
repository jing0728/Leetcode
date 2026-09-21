class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}   # 前缀和为0出现过1次（重要！）
        count=0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num              # 累加前缀和
            complement = prefix_sum - k    # 找搭档
            if complement in map:          # 查表
                count += map[complement]   # 加上出现次数
            map[prefix_sum] = map.get(prefix_sum, 0) + 1
        return count           
            