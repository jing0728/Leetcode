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