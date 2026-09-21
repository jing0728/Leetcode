class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map={}
        for i in ransomNote:
            map[i]=map.get(i,0)+1
        for i in magazine:
            map[i]=map.get(i,0)-1
        for i in map.values():
            if i > 0:
                return False
        return True
    
