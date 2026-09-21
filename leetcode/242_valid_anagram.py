class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for i in s:
            map[i]=map.get(i,0)+1# map.i(char, 0) 意思是：
                                # 如果 i 在字典里就返回它的值，不在就返回默认值 0
        for i in t:
            map[i]=map.get(i,0)-1
        for i in map.values():
            if i !=0:
                return False
        return True
# map.keys()    # → 所有的键：["a", "r", "t"]
# map.values()  # → 所有的值：[3, 0, 1]
# map.items()   # → 键值对一起：[("a",3), ("r",0), ("t",1)]

def is_anagram(s, t):
    return sorted(s)==sorted(t)
print(is_anagram("anagram", "nagaram"))   # 期望 True
print(is_anagram("rat", "car"))           # 期望 False
print(is_anagram("aacc", "ccac"))         # 期望 False
print(is_anagram("", ""))                 # 期望 True


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