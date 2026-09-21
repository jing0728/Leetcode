def frequency_sort(s):
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
print(frequency_sort(""))         # 期望 空字符串，屏幕上是一个空行