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

def contains_duplicate(nums):
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

"""def is_anagram(s, t):
    if sorted(s)==sorted(t):
        return True
    else:
        return False
    return sorted(s)==sorted(t)
print(is_anagram("anagram", "nagaram"))   # 期望 True
print(is_anagram("rat", "car"))           # 期望 False
print(is_anagram("aacc", "ccac"))         # 期望 False
print(is_anagram("", ""))                 # 期望 True"""

"""def is_anagram(s, t):
    s1={}
    t1={}
    for letter in s:
        if letter in s1:
            s1[letter]+=1
        else:
            s1[letter]=1
    for letter in t:
        if letter in t1:
            t1[letter]+=1
        else:
            t1[letter]=1
    return s1==t1
print(is_anagram("anagram", "nagaram"))   # 期望 True
print(is_anagram("rat", "car"))           # 期望 False
print(is_anagram("aacc", "ccac"))         # 期望 False
print(is_anagram("", ""))                 # 期望 True"""

"""def first_unique_char(s):
    s1={}
    for i, letter in enumerate(s):
        if letter in s1:
            s1[letter] += 1
        else:
            s1[letter] = 1
    for i, letter in enumerate(s):
        if s1[letter] == 1:
            return i
    return -1
    pass
print(first_unique_char("leetcode"))      # 期望 0
print(first_unique_char("loveleetcode"))  # 期望 2
print(first_unique_char("aabb"))          # 期望 -1
print(first_unique_char(""))              # 期望 -1"""

"""def majority_element(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num in nums:
        if count[num]>len(nums)/2:
            return num
print(majority_element([3, 2, 3]))          # 期望 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 期望 2
print(majority_element([5]))                # 期望 5"""

"""def most_frequent(nums):
    count={}
    max_count=0
    answer = None
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num in nums:
        if count[num] > max_count:
            max_count=count[num]
            answer = num
    return answer
print(most_frequent([1, 1, 1, 2, 2, 3]))   # 期望 1
print(most_frequent([4, 4, 2, 2, 2, 3]))   # 期望 2
print(most_frequent([7]))                   # 期望 7"""



def topKFrequent(self, nums, k):
    count={}
    i=0
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return(sorted_count[:k])


                