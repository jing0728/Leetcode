"""def reverse_string(s):
    s[:]=s[::-1]
    return s


s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

"""def reverse_string(s):
    new=[]
    le=len(s)
    for i,ch in enumerate(s):
        new.append(s[le-1-i])
    s[:]=new
    return s



s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]"""

def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]

def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[right],s[left]=s[left],s[right]
        right-=1
        left+=1

s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)
# 期望 ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)
# 期望 ["h", "a", "n", "n", "a", "H"]