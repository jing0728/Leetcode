#hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num]=1
        return False


"""def contains_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))                     # 期望 True
print(contains_duplicate([1, 2, 3, 4]))                     # 期望 False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))   # 期望 True
print(contains_duplicate([]))                               # 期望 False"""