"""class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for word in strs:
            key=tuple(sorted(word))
            map[key] = map.get(key, []) + [word]
            # 如果 key 存在，取出已有列表再加上新词
            # 如果 key 不存在，默认空列表 [] 再加上新词
        return list(map.values())"""

"""def group_anagrams(words):
    map={}
    for word in words:
        key=tuple(sorted(word))
        map[key]=map.get(key,[])+[word]
    return list(map.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# 期望 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""]))     # 期望 [['']]
print(group_anagrams(["a"]))    # 期望 [['a']]"""

def group_anagrams(words):
    map={}
    for word in words:
        ranked=str(sorted(word))
        map[ranked]=map.get(ranked,[])+[word]
    return list(map.values())
    pass

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# 期望 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""]))     # 期望 [['']]
print(group_anagrams(["a"]))    # 期望 [['a']]