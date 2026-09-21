"""def first_unique_char(s):
    unique={}
    for letter in s:
        unique[letter]=unique.get(letter,0)+1
    for i,letter in enumerate(s):
        if unique[letter]==1:
            return i
    return -1
print(first_unique_char("leetcode"))      # 期望 0
print(first_unique_char("loveleetcode"))  # 期望 2
print(first_unique_char("aabb"))          # 期望 -1
print(first_unique_char(""))              # 期望 -1"""

def top_k_frequent(nums, k):
    count={}
    for num in nums:
        count[num]=count.get(num,0)+1
    count=sorted(count.items(),key=lambda num:num[1],reverse=True)
    ans = count[:k]
    new =[]
 
    for num in ans:
        new.append(num[0])
    return (new)
    

        

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))   # 期望 [1, 2]
print(top_k_frequent([1], 1))                   # 期望 [1]
print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))   # 期望 [6]