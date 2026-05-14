class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for i in s:
            map[i]=map.get(i,0)+1
        for i in t:
            map[i]=map.get(i,0)-1
        for i in map.values():
            if i !=0:
                return False
        return True
