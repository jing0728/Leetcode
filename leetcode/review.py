# # # ########2026-09-18#########
# # # """def first_unique_char(s):
# # #     unique={}
# # #     for letter in s:
# # #         unique[letter]=unique.get(letter,0)+1
# # #     for i,letter in enumerate(s):
# # #         if unique[letter]==1:
# # #             return i
# # #     return -1
# # # print(first_unique_char("leetcode"))      # 期望 0
# # # print(first_unique_char("loveleetcode"))  # 期望 2
# # # print(first_unique_char("aabb"))          # 期望 -1
# # # print(first_unique_char(""))              # 期望 -1"""

# # # """def top_k_frequent(nums, k):
# # #     count={}
# # #     for num in nums:
# # #         count[num]=count.get(num,0)+1
# # #     count=sorted(count.items(),key=lambda num:num[1],reverse=True)
# # #     ans = count[:k]
# # #     new =[]
# # #     for num in ans:
# # #         new.append(num[0])
# # #     return (new)   

# # # print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))   # 期望 [1, 2]
# # # print(top_k_frequent([1], 1))                   # 期望 [1]
# # # print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))   # 期望 [6]"""


# # # ########2026-09-21#########
# # # """def top_k_frequent(nums, k):
# # #     count={}
# # #     for num in nums:
# # #         count[num]=count.get(num,0)+1
# # #     count=sorted(count.items(),key=lambda num:num[1],reverse=True)
# # #     ans = count[:k]
# # #     new =[]
# # #     for num in ans:
# # #         new.append(num[0])
# # #     return (new)   

# # # print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))   # 期望 [1, 2]
# # # print(top_k_frequent([1], 1))                   # 期望 [1]
# # # print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))   # 期望 [6]"""

# # # """def frequency_sort(s):
# # #     count={}
# # #     for letter in s:
# # #         count[letter]=count.get(letter,0)+1
# # #     ranked =sorted(count.items(),key= lambda num:num[1],reverse=True)
# # #     new=""
# # #     for letter,frq in ranked:
# # #         new+=(letter[0]*frq)
# # #     return (new)

# # # print(frequency_sort("tree"))     # 期望 eetr 或 eert
# # # print(frequency_sort("cccaaa"))   # 期望 cccaaa 或 aaaccc
# # # print(frequency_sort("Aabb"))     # 期望 bbAa 或 bbaA
# # # print(frequency_sort(""))         # 期望 空字符串，屏幕上是一个空行"""

# # # """count[letter]=count.get(letter,0)+1
# # # ranked = sorted(count.items(),key= lambda letter:letter[0],reverse=True)"""

# # # ########2026-09-22#########
# # # """def two_sum(nums, target):
# # #     count={}
# # #     for i,num in enumerate(nums):
# # #         need =target-num
# # #         if need in count:
# # #             return [count[need],i]
# # #         count[num]=i

# # # print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]
# # # print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]
# # # print(two_sum([3, 3], 6))           # 期望 [0, 1]
# # # """

# # # """def contains_duplicate(nums):
# # #     count={}
# # #     for num in nums:
# # #         count[num]=count.get(num,0)+1
# # #         if count[num]>=2:
# # #             return True
# # #     return False

# # # print(contains_duplicate([1, 2, 3, 1]))                     # 期望 True
# # # print(contains_duplicate([1, 2, 3, 4]))                     # 期望 False
# # # print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))   # 期望 True
# # # print(contains_duplicate([]))                               # 期望 False"""

# # # """def is_anagram(s, t):
# # #     return sorted(s)==sorted(t)

# # # print(is_anagram("anagram", "nagaram"))   # 期望 True
# # # print(is_anagram("rat", "car"))           # 期望 False
# # # print(is_anagram("aacc", "ccac"))         # 期望 False
# # # print(is_anagram("", ""))                 # 期望 True"""

# # # """def is_anagram(s, t):
# # #     count_s={}
# # #     count_t={}
# # #     for l in s:
# # #         count_s[l]=count_s.get(l,0)+1
# # #     for l in t:
# # #         count_t[l]=count_t.get(l,0)+1
# # #     return count_t==count_s

# # # print(is_anagram("anagram", "nagaram"))   # 期望 True
# # # print(is_anagram("rat", "car"))           # 期望 False
# # # print(is_anagram("aacc", "ccac"))         # 期望 False
# # # print(is_anagram("", ""))                 # 期望 True"""

# # # """def first_unique_char(s):
# # #     count={}
# # #     for ch in s:
# # #         count[ch]=count.get(ch,0)+1
# # #     for i,ch in enumerate(s):
# # #         if count[ch]==1:
# # #             return i
# # #     return -1


# # # print(first_unique_char("leetcode"))      # 期望 0
# # # print(first_unique_char("loveleetcode"))  # 期望 2
# # # print(first_unique_char("aabb"))          # 期望 -1
# # # print(first_unique_char(""))              # 期望 -1"""

# # # """def majority_element(nums):
# # #     count={}
# # #     for num in nums:
# # #         count[num]=count.get(num,0)+1
# # #     for num in nums:
# # #         if count[num]>len(nums)/2:
# # #             return num
# # #     pass

# # # print(majority_element([3, 2, 3]))              # 期望 3
# # # print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 期望 2
# # # print(majority_element([5]))                    # 期望 5"""

# # # """def top_k_frequent(nums, k):
# # #     count={}
# # #     ans=[]
# # #     for num in nums:
# # #         count[num]=count.get(num,0)+1
# # #     ranked=sorted(count.items(),key=lambda num:num[1],reverse=True)
# # #     for num,frq in ranked[:k]:
# # #         ans.append(num)
# # #     return ans


# # # print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))          # 期望 [1, 2]
# # # print(top_k_frequent([1], 1))                          # 期望 [1]
# # # print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))     # 期望 [6]"""

# # # """def frequency_sort(s):
# # #     count={}
# # #     ans=""
# # #     for ch in s:
# # #         count[ch]=count.get(ch,0)+1
# # #     ranked=sorted(count.items(),key=lambda pair:pair[1],reverse=True)
# # #     for ch,frq in ranked:
# # #         ans+=(ch*frq)
# # #     return ans

# # # print(frequency_sort("tree"))     # 期望 eetr 或 eert
# # # print(frequency_sort("cccaaa"))   # 期望 cccaaa 或 aaaccc
# # # print(frequency_sort("Aabb"))     # 期望 bbAa 或 bbaA
# # # print(frequency_sort(""))         # 期望 空字符串"""

# # # def group_anagrams(words):
# # #     count={}
# # #     for word in words:
# # #         ranked =tuple(sorted(word))
# # #         count[ranked]=count.get(ranked,[])+[word]
# # #     return list(count.values())

# # # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# # # # 期望 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# # # print(group_anagrams([""]))     # 期望 [['']]
# # # print(group_anagrams(["a"]))    # 期望 [['a']]

# # """def reverse_string(s):
# #     s[:]=s[::-1]
# #     return s


# # s1 = ["h", "e", "l", "l", "o"]
# # reverse_string(s1)
# # print(s1)
# # # 期望 ["o", "l", "l", "e", "h"]

# # s2 = ["H", "a", "n", "n", "a", "h"]
# # reverse_string(s2)
# # print(s2)
# # # 期望 ["h", "a", "n", "n", "a", "H"]"""

# # """def reverse_string(s):
# #     new=[]
# #     le=len(s)
# #     for i,ch in enumerate(s):
# #         new.append(s[le-1-i])
# #     s[:]=new
# #     return s



# # s1 = ["h", "e", "l", "l", "o"]
# # reverse_string(s1)
# # print(s1)
# # # 期望 ["o", "l", "l", "e", "h"]

# # s2 = ["H", "a", "n", "n", "a", "h"]
# # reverse_string(s2)
# # print(s2)
# # # 期望 ["h", "a", "n", "n", "a", "H"]"""

# # """def reverse_string(s):
# #     left=0
# #     right=len(s)-1
# #     while left<right:
# #         s[left], s[right] = s[right], s[left]
# #         left += 1
# #         right -= 1
# #     return s

# # s1 = ["h", "e", "l", "l", "o"]
# # reverse_string(s1)
# # print(s1)
# # # 期望 ["o", "l", "l", "e", "h"]

# # s2 = ["H", "a", "n", "n", "a", "h"]
# # reverse_string(s2)
# # print(s2)
# # # 期望 ["h", "a", "n", "n", "a", "H"]"""

# # """def reverse_string(s):
# #     left=0
# #     right=len(s)-1
# #     while left<right:
# #         s[right],s[left]=s[left],s[right]
# #         right-=1
# #         left+=1

# # s1 = ["h", "e", "l", "l", "o"]
# # reverse_string(s1)
# # print(s1)
# # # 期望 ["o", "l", "l", "e", "h"]

# # s2 = ["H", "a", "n", "n", "a", "h"]
# # reverse_string(s2)
# # print(s2)
# # # 期望 ["h", "a", "n", "n", "a", "H"]"""

# # """def two_sum_sorted(numbers, target):
# #     left=0
# #     right=len(numbers)-1
# #     while left<right:
# #         total = numbers[left]+numbers[right]
# #         if total==target:
# #             return [left+1,right+1]
# #         elif total>target:
# #             right-=1
# #         else:
# #             left+=1
            


# # print(two_sum_sorted([2, 7, 11, 15], 9))
# # # 期望 [1, 2]

# # print(two_sum_sorted([2, 3, 4], 6))
# # # 期望 [1, 3]

# # print(two_sum_sorted([-1, 0], -1))
# # # 期望 [1, 2]"""

# # """def move_zeroes(nums):
# #     left=0
# #     while left<(len(nums)-1):
# #         if nums[left]==0:
# #             nums.pop(left)
# #             nums.append(0)
# #         left+=1
# #     return nums



# # nums1 = [0, 1, 0, 3, 12]
# # move_zeroes(nums1)
# # print(nums1)
# # # 期望 [1, 3, 12, 0, 0]

# # nums2 = [0]
# # move_zeroes(nums2)
# # print(nums2)
# # # 期望 [0]

# # nums3 = [1, 0, 2, 0, 3]
# # move_zeroes(nums3)
# # print(nums3)
# # # 期望 [1, 2, 3, 0, 0]"""

# # """def move_zeroes(nums):
# #     left=0
# #     for right in range(len(nums)):
# #         if nums[right] !=0:
# #             nums[left],nums[right]=nums[right],nums[left]
# #             left+=1
# #     return nums

# # nums1 = [0, 1, 0, 3, 12]
# # move_zeroes(nums1)
# # print(nums1)
# # # 期望 [1, 3, 12, 0, 0]

# # nums2 = [0]
# # move_zeroes(nums2)
# # print(nums2)
# # # 期望 [0]

# # nums3 = [1, 0, 2, 0, 3]
# # move_zeroes(nums3)
# # print(nums3)
# # # 期望 [1, 2, 3, 0, 0]"""

# # def sorted_squares(nums):
# #     left=0
# #     for right in range(len(nums)):
# #         if abs(nums[right])<abs(nums[left]):
# #             nums[left],nums[right]=nums[right],nums[left]
# #             left+=1
# #     return nums


# # print(sorted_squares([-4, -1, 0, 3, 10]))
# # # 期望 [0, 1, 9, 16, 100]

# # print(sorted_squares([-7, -3, 2, 3, 11]))
# # # 期望 [4, 9, 9, 49, 121]

# # print(sorted_squares([0]))
# # # 期望 [0]

# ########2026-09-23#########

# """def contains_duplicate(nums):
#     count={}
#     for num in nums:
#         count[num]=count.get(num,0)+1
#         if count[num]>=2:
#             return True
#     return False
#     pass


# print(contains_duplicate([1, 2, 3, 1]))
# # 期望 True

# print(contains_duplicate([1, 2, 3, 4]))
# # 期望 False

# print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# # 期望 True

# print(contains_duplicate([]))
# # 期望 False"""

# """def is_anagram(s, t):
#     return sorted(s)==sorted(t)

# print(is_anagram("anagram", "nagaram"))
# # 期望 True

# print(is_anagram("rat", "car"))
# # 期望 False

# print(is_anagram("aacc", "ccac"))
# # 期望 False

# print(is_anagram("", ""))"""
# # 期望 True

# """def is_anagram(s, t):
#     count_s={}
#     count_t={}
#     for ch in s:
#         count_s[ch]=count_s.get(ch,0)+1
#     for ch in t:
#         count_t[ch]=count_t.get(ch,0)+1
#     ranked_s=sorted(count_s.items(),key=lambda x:x[0],reverse=True)
#     ranked_t=sorted(count_t.items(),key=lambda x:x[0],reverse=True)
#     return ranked_s==ranked_t

# print(is_anagram("anagram", "nagaram"))
# # 期望 True

# print(is_anagram("rat", "car"))
# # 期望 False

# print(is_anagram("aacc", "ccac"))
# # 期望 False

# print(is_anagram("", ""))
# # 期望 True"""

# """def first_unique_char(s):
#     count={}
#     for ch in s:
#         count[ch]=count.get(ch,0)+1
#     for i,ch in enumerate(s):
#         if count[ch]==1:
#             return i
#     return -1

#     pass


# print(first_unique_char("leetcode"))
# # 期望 0

# print(first_unique_char("loveleetcode"))
# # 期望 2

# print(first_unique_char("aabb"))
# # 期望 -1

# print(first_unique_char(""))
# # 期望 -1"""

# """def majority_element(nums):
#     count={}
#     for num in nums:
#         count[num]=count.get(num,0)+1
#     for num in nums:
#         if count[num]>len(nums)/2:
#             return num
#     pass


# print(majority_element([3, 2, 3]))
# # 期望 3

# print(majority_element([2, 2, 1, 1, 1, 2, 2]))
# # 期望 2

# print(majority_element([5]))
# # 期望 5"""

# """def top_k_frequent(nums, k):
#     count={}
#     for num in nums:
#         count[num]=count.get(num,0)+1
#     ranked= sorted(count.items(),key=lambda x:x[1],reverse=True)
#     ans=[]
#     for num,frq in ranked[:k]:
#         ans.append(num)
#     return ans


# print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
# # 期望 [1, 2]

# print(top_k_frequent([1], 1))
# # 期望 [1]

# print(top_k_frequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 2))
# # 期望 [6, 4]"""

# # def group_anagrams(words):
# #     count={}
# #     for ch in words:
# #         ranked=str(sorted(ch))
# #         count[ranked]=count.get(ranked,[])+[ch]
# #     return list(count.values())

# # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# # # 期望 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# # print(group_anagrams([""]))
# # # 期望 [['']]

# # print(group_anagrams(["a"]))
# # # 期望 [['a']]

# # def is_isomorphic(s, t):
# #     s_to_t={}
# #     t_to_s={}
# #     for a,b in zip(s,t):
# #         if a in s_to_t:
# #             if s_to_t[a]!=b:
# #                 return False
# #         else:
# #             s_to_t[a]=b
# #         if b in t_to_s:
# #             if t_to_s[b] != a:
# #                 return False
# #         else:
# #             t_to_s[b] = a
# #     return True


# # print(is_isomorphic("egg", "add"))
# # # 期望 True

# # print(is_isomorphic("foo", "bar"))
# # # 期望 False

# # print(is_isomorphic("paper", "title"))
# # # 期望 True

# # print(is_isomorphic("ab", "aa"))
# # # 期望 False

# def word_pattern(pattern, s):
#     s=s.split()
#     p_to_s={}
#     s_to_p={}
#     if len(pattern) != len(s):
#         return False
#     for a,b in zip(pattern,s):
#         if a in s_to_p:
#             if s_to_p[a]!=b:
#                 return False
#         else:
#             s_to_p[a]=b
#         if b in p_to_s:
#             if p_to_s[b] != a:
#                 return False
#         else:
#             p_to_s[b] = a
#     return True


# print(word_pattern("abba", "dog cat cat dog"))
# # 期望 True

# print(word_pattern("abba", "dog cat cat fish"))
# # 期望 False

# print(word_pattern("aaaa", "dog cat cat dog"))
# # 期望 False

# print(word_pattern("abba", "dog dog dog dog"))
# # 期望 False

# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         s=s.split()
#         pattern_to_word={}
#         word_to_pattern={}
#         if len(pattern)!=len(s):
#             return False
#         for a,b in zip(pattern,s):
#             pattern_to_word[a]=pattern_to_word.get(a,b)
#             if pattern_to_word[a]!=b:
#                 return False
#             word_to_pattern[b]=word_to_pattern.get(b,a)
#             if word_to_pattern[b]!=a:
#                     return False

########2026-09-24#########

# def contains_nearby_duplicate(nums, k):
# #     cout={}
# #     for i,num in enumerate(nums):
# #         if num in cout:
# #             if abs(cout[num]-i)<=k:
# #                 return True
# #         cout[num]=i
# #     return False



# # print(contains_nearby_duplicate([1, 2, 3, 1], 3))
# # # 期望 True

# # print(contains_nearby_duplicate([1, 0, 1, 1], 1))
# # # 期望 True

# # print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
# # # 期望 False

# # print(contains_nearby_duplicate([1, 2, 3, 1], 2))
# # # 期望 False

# # print(contains_nearby_duplicate([], 0))
# # # 期望 False

# # def is_happy(n):
# #     same=set()
# #     while n!=1:
# #         if n in same:
# #             return False
# #         same.add(n)
# #         total=0
# #         for i in str(n):
# #             total+=int(i)**2
# #         n=total
# #     return True


# # print(is_happy(19))
# # # 期望 True

# # print(is_happy(2))
# # # 期望 False

# # print(is_happy(1))
# # # 期望 True

# # print(is_happy(7))
# # # 期望 True


# # def is_palindrome(s):
# #     word=''.join(filter(str.isalnum,s)).lower()
# #     return word==word[::-1]


# # print(is_palindrome("A man, a plan, a canal: Panama"))
# # # 期望 True

# # print(is_palindrome("race a car"))
# # # 期望 False

# # print(is_palindrome(" "))
# # # 期望 True

# # print(is_palindrome("0P"))
# # # 期望 False

# # def sorted_squares(nums):
# #     ans = [0] * len(nums)

# #     left = 0
# #     right = len(nums) - 1
# #     pos = len(nums) - 1

# #     while left <= right:
# #         if abs(nums[left]) > abs(nums[right]):
# #             ans[pos]=nums[left]**2
# #             left+=1
# #         else:
# #             ans[pos]=nums[right]**2
# #             right-=1

# #         pos -= 1

# #     return ans
        

# # print(sorted_squares([-4, -1, 0, 3, 10]))
# # # 期望 [0, 1, 9, 16, 100]

# # print(sorted_squares([-7, -3, 2, 3, 11]))
# # # 期望 [4, 9, 9, 49, 121]

# # print(sorted_squares([0]))
# # # 期望 [0]

# # print(sorted_squares([-5, -3, -2, -1]))
# # # 期望 [1, 4, 9, 25]

# # def max_area(height):
# #     left=0
# #     right=len(height)-1
# #     ans=[]
# #     while left<right:
# #         area = min(height[left], height[right]) * (right - left)
# #         ans.append(area)
# #         if height[left] < height[right]:
# #             left += 1
# #         else:
# #             right -= 1
# #     return max(ans)

# # print(max_area([1,8,6,2,5,4,8,3,7]))
# # # 期望 49

# # print(max_area([1,1]))
# # # 期望 1

# # print(max_area([4,3,2,1,4]))
# # # 期望 16

# # print(max_area([1,2,1]))
# # # 期望 2

# # def three_sum(nums):
# #     nums.sort()
# #     ans=set()
# #     for i in range(len(nums)):
# #         left=i+1
# #         right=len(nums)-1
# #         while left<right:
# #             total=nums[i]+nums[left]+nums[right]
# #             if total<0:
# #                 left+=1
# #             elif total>0:
# #                 right-=1
# #             else:
# #                 ans.add((nums[i],nums[left],nums[right]))
# #                 left+=1
# #                 right-=1
# #     return  [list(x) for x in ans]


# # print(three_sum([-1, 0, 1, 2, -1, -4]))
# # # 期望 [[-1, -1, 2], [-1, 0, 1]]

# # print(three_sum([0, 1, 1]))
# # # 期望 []

# # print(three_sum([0, 0, 0]))
# # # 期望 [[0, 0, 0]]

# # def remove_duplicates(nums):
# #     left=1
# #     for right in range(len(nums)):
# #         if nums[right]!=nums[right-1]:
# #             nums[left]=nums[right]
# #             left+=1
# #     return left



# # nums1 = [1, 1, 2]
# # k1 = remove_duplicates(nums1)
# # print(k1)
# # print(nums1[:k1])
# # # 期望：
# # # 2
# # # [1, 2]

# # nums2 = [0,0,1,1,1,2,2,3,3,4]
# # k2 = remove_duplicates(nums2)
# # print(k2)
# # print(nums2[:k2])
# # # 期望：
# # # 5
# # # [0, 1, 2, 3, 4]

# def remove_element(nums, val):
#     left=0
#     for right in range(len(nums)):
#         if nums[right]!=val:
#             nums[left]=nums[right]
#             left+=1
            
#     return left



# nums1 = [3, 2, 2, 3]
# k1 = remove_element(nums1, 3)
# print(k1)
# print(nums1[:k1])
# # 期望：
# # 2
# # [2, 2]


# nums2 = [0,1,2,2,3,0,4,2]
# k2 = remove_element(nums2, 2)
# print(k2)
# print(nums2[:k2])
# # 期望：
# # 5
# # [0,1,3,0,4]

########2026-09-30#########
# def contains_duplicate(nums):
#     count={}
#     for num in nums:
#         count[num]=count.get(num,0)+1
#         if count[num]>1:
#             return True
#     return False
# print(contains_duplicate([1, 2, 3, 1]))     # True
# print(contains_duplicate([1, 2, 3, 4]))     # False
# print(contains_duplicate([]))                # False

# def two_sum(nums, target):
#     conut={}
#     for i,num in enumerate(nums):
#         need =target -num
#         if need in conut:
#             return [conut[need],i]
#         else:
#             conut[num]=i
#     pass


# print(two_sum([2, 7, 11, 15], 9))
# # 期望 [0, 1]

# print(two_sum([3, 2, 4], 6))
# # 期望 [1, 2]

# print(two_sum([3, 3], 6))
# # 期望 [0, 1]

########2026-10-09#########

# def two_sum(nums,target):
#     ans={}
#     for i,num in enumerate(nums):
#         need = target - num
#         if need in ans:
#             return [ans[need],i]
#         ans[num]=i

# def merge(interval):
#     interval.sort()
#     result = [interval[0]]
#     for interval in interval[1:]:
#         last = result[-1]              # 取 result 里最后一个区间
#         if interval[0] <= last[1]:   # 0 还是 1？
#             last[1] = max(last[1],interval[1])       # 填什么表达式
#         else:
#             result.append(interval)
#     return result

# print(merge([[1,5],[5,9],[7,8],[6,7],[3,7]]))   # 期望 [[1, 9]]
# print(merge([[1,5],[3,4],[6,9]]))                # 期望 [[1, 5], [6, 9]]

########2026-10-15#########
# def two_sum(nums,target):
#     ans={}
#     for i,num in enumerate(nums):
#         need = target -num
#         if need in ans:
#             return [ans[need],i]
#         ans[num]=i

# print(two_sum([2, 7, 11, 15], 9))   # 期望 [0, 1]
# print(two_sum([3, 2, 4], 6))        # 期望 [1, 2]
# print(two_sum([3, 3], 6))           # 期望 [0, 1]

# def contains_duplicate(nums):
#     ans=set()
#     for num in nums:
#         if num in ans:
#             return True
#         ans.add(num)
#     return False
# print(contains_duplicate([1, 2, 3, 1]))                     # 期望 True
# print(contains_duplicate([1, 2, 3, 4]))                     # 期望 False
# print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))   # 期望 True
# print(contains_duplicate([]))                               # 期望 False

# def is_anagram(s,t):
#     return sorted(s)==sorted(t)
# print(is_anagram("anagram", "nagaram"))   # 期望 True
# print(is_anagram("rat", "car"))           # 期望 False
# print(is_anagram("aacc", "ccac"))         # 期望 False
# print(is_anagram("", ""))                 # 期望 True

# def is_anagram(s,t):
#     ans_t={}
#     ans_s={}
#     for letter in s:
#         ans_s[letter]=ans_s.get(letter,0)+1
#     for letter in t:
#         ans_t[letter]=ans_t.get(letter,0)+1
#     return ans_s==ans_t
# print(is_anagram("anagram", "nagaram"))   # 期望 True
# print(is_anagram("rat", "car"))           # 期望 False
# print(is_anagram("aacc", "ccac"))         # 期望 False
# print(is_anagram("", ""))                 # 期望 True

# def first_unique_char(s):
#     ans={}
#     for letter in s:
#         ans[letter]=ans.get(letter,0)+1
#     for i,letter in enumerate(s):
#         if ans[letter]==1:
#             return i
#     return -1
# print(first_unique_char("leetcode"))      # 期望 0
# print(first_unique_char("loveleetcode"))  # 期望 2
# print(first_unique_char("aabb"))          # 期望 -1
# print(first_unique_char(""))              # 期望 -1

# def majority_element(nums):
#     ans={}
#     for num in nums:
#         ans[num]=ans.get(num,0)+1
#         if ans[num]>len(nums)/2:
#             return num
# print(majority_element([3, 2, 3]))              # 期望 3
# print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 期望 2
# print(majority_element([5]))                    # 期望 5

# def reverse_string(s):
#     left=0
#     right=len(s)-1
#     while left<right:
#         s[left],s[right]=s[right],s[left]
#         right-=1
#         left+=1
#     return s
# s1 = ["h", "e", "l", "l", "o"]
# reverse_string(s1)
# print(s1)   # 期望 ["o", "l", "l", "e", "h"]

# s2 = ["H", "a", "n", "n", "a", "h"]
# reverse_string(s2)
# print(s2)   # 期望 ["h", "a", "n", "n", "a", "H"]

# def two_sum_sorted(numbers,target):
#     left=0
#     right=len(numbers)-1
#     while left<right:
#         sum=numbers[left]+numbers[right]
#         if sum==target:
#             return [left+1,right+1]
#         elif sum>target:
#             right-=1
#         else:
#             left+=1


# print(two_sum_sorted([2, 7, 11, 15], 9))   # 期望 [1, 2]
# print(two_sum_sorted([2, 3, 4], 6))        # 期望 [1, 3]
# print(two_sum_sorted([-1, 0], -1))         # 期望 [1, 2]

# def move_zeroes(nums):
#     count=list.count(0)
    




# nums1 = [0, 1, 0, 3, 12]
# move_zeroes(nums1)
# print(nums1)   # 期望 [1, 3, 12, 0, 0]

# nums2 = [0]
# move_zeroes(nums2)
# print(nums2)   # 期望 [0]

# nums3 = [1, 0, 2, 0, 3]
# move_zeroes(nums3)
# print(nums3)   # 期望 [1, 2, 3, 0, 0]       
        
