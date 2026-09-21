def first_unique_char(s):
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
print(first_unique_char(""))              # 期望 -1