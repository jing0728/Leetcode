class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for word in strs:
            key=tuple(sorted(word))
            map[key] = map.get(key, []) + [word]
            # 如果 key 存在，取出已有列表再加上新词
            # 如果 key 不存在，默认空列表 [] 再加上新词
        return list(map.values())
