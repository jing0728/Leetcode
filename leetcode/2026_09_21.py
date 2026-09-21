"""def top_k_frequent(nums, k):
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
print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))   # 期望 [6]"""

"""def frequency_sort(s):
    count={}
    for letter in s:
        count[letter]=count.get(letter,0)+1
    ranked =sorted(count.items(),key= lambda num:num[1],reverse=True)
    new=""
    for letter,frq in ranked:
        new+=(letter[0]*frq)
    return (new)

print(frequency_sort("tree"))     # 期望 eetr 或 eert
print(frequency_sort("cccaaa"))   # 期望 cccaaa 或 aaaccc
print(frequency_sort("Aabb"))     # 期望 bbAa 或 bbaA
print(frequency_sort(""))         # 期望 空字符串，屏幕上是一个空行"""

"""count[letter]=count.get(letter,0)+1
ranked = sorted(count.items(),key= lambda letter:letter[0],reverse=True)"""