"""def contains_duplicate(nums):
    count={}
    for num in nums:
        count[num]=count.get(num,0)+1
        if count[num]>=2:
            return True
    return False
    pass


print(contains_duplicate([1, 2, 3, 1]))
# 期望 True

print(contains_duplicate([1, 2, 3, 4]))
# 期望 False

print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# 期望 True

print(contains_duplicate([]))
# 期望 False"""

"""def is_anagram(s, t):
    return sorted(s)==sorted(t)

print(is_anagram("anagram", "nagaram"))
# 期望 True

print(is_anagram("rat", "car"))
# 期望 False

print(is_anagram("aacc", "ccac"))
# 期望 False

print(is_anagram("", ""))"""
# 期望 True

"""def is_anagram(s, t):
    count_s={}
    count_t={}
    for ch in s:
        count_s[ch]=count_s.get(ch,0)+1
    for ch in t:
        count_t[ch]=count_t.get(ch,0)+1
    ranked_s=sorted(count_s.items(),key=lambda x:x[0],reverse=True)
    ranked_t=sorted(count_t.items(),key=lambda x:x[0],reverse=True)
    return ranked_s==ranked_t

print(is_anagram("anagram", "nagaram"))
# 期望 True

print(is_anagram("rat", "car"))
# 期望 False

print(is_anagram("aacc", "ccac"))
# 期望 False

print(is_anagram("", ""))
# 期望 True"""

"""def first_unique_char(s):
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    for i,ch in enumerate(s):
        if count[ch]==1:
            return i
    return -1

    pass


print(first_unique_char("leetcode"))
# 期望 0

print(first_unique_char("loveleetcode"))
# 期望 2

print(first_unique_char("aabb"))
# 期望 -1

print(first_unique_char(""))
# 期望 -1"""

"""def majority_element(nums):
    count={}
    for num in nums:
        count[num]=count.get(num,0)+1
    for num in nums:
        if count[num]>len(nums)/2:
            return num
    pass


print(majority_element([3, 2, 3]))
# 期望 3

print(majority_element([2, 2, 1, 1, 1, 2, 2]))
# 期望 2

print(majority_element([5]))
# 期望 5"""

"""def top_k_frequent(nums, k):
    count={}
    for num in nums:
        count[num]=count.get(num,0)+1
    ranked= sorted(count.items(),key=lambda x:x[1],reverse=True)
    ans=[]
    for num,frq in ranked[:k]:
        ans.append(num)
    return ans


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
# 期望 [1, 2]

print(top_k_frequent([1], 1))
# 期望 [1]

print(top_k_frequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 2))
# 期望 [6, 4]"""

# def group_anagrams(words):
#     count={}
#     for ch in words:
#         ranked=str(sorted(ch))
#         count[ranked]=count.get(ranked,[])+[ch]
#     return list(count.values())

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# # 期望 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# print(group_anagrams([""]))
# # 期望 [['']]

# print(group_anagrams(["a"]))
# # 期望 [['a']]

# def is_isomorphic(s, t):
#     s_to_t={}
#     t_to_s={}
#     for a,b in zip(s,t):
#         if a in s_to_t:
#             if s_to_t[a]!=b:
#                 return False
#         else:
#             s_to_t[a]=b
#         if b in t_to_s:
#             if t_to_s[b] != a:
#                 return False
#         else:
#             t_to_s[b] = a
#     return True


# print(is_isomorphic("egg", "add"))
# # 期望 True

# print(is_isomorphic("foo", "bar"))
# # 期望 False

# print(is_isomorphic("paper", "title"))
# # 期望 True

# print(is_isomorphic("ab", "aa"))
# # 期望 False

def word_pattern(pattern, s):
    s=s.split()
    p_to_s={}
    s_to_p={}
    if len(pattern) != len(s):
        return False
    for a,b in zip(pattern,s):
        if a in s_to_p:
            if s_to_p[a]!=b:
                return False
        else:
            s_to_p[a]=b
        if b in p_to_s:
            if p_to_s[b] != a:
                return False
        else:
            p_to_s[b] = a
    return True


print(word_pattern("abba", "dog cat cat dog"))
# 期望 True

print(word_pattern("abba", "dog cat cat fish"))
# 期望 False

print(word_pattern("aaaa", "dog cat cat dog"))
# 期望 False

print(word_pattern("abba", "dog dog dog dog"))
# 期望 False