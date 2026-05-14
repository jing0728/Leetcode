class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:          # 数组为空直接返回0
            return 0
        
        new = sorted(nums)
        longest = 1           # 最长长度，至少是1
        length = 1            # 当前连续长度

        for i in range(1, len(new)):
            if new[i] == new[i-1] + 1:    # 和前一个差1，连续
                length += 1
            elif new[i] == new[i-1]:       # 遇到重复数字，跳过
                continue
            else:                          # 断了，重新开始
                longest = max(longest, length)
                length = 1

        return max(longest, length)        
    
#hashmap
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)   # 把所有数存进去
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:       # 是起点才开始数
                length = 1
                while num + length in num_set:  # 一直往后找
                    length += 1
                longest = max(longest, length)

        return longest