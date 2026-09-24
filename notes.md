"12".isdigit()      # True，是不是全是数字
"abc".isalpha()     # True，是不是全是字母
"   ".isspace()     # True，是不是全是空白
"abc123".isalnum()  # True，是不是全是字母或数字

"  hi  ".lstrip()   # "hi  "   只去左边（left）
"  hi  ".rstrip()   # "  hi"   只去右边（right）
"  hi  ".strip()    # "hi"     两边都去


count[num]=count.get(num,0)+1   #去字典 count 里找键 num 对应的值，找到就给我那个值，找不到就给我 0

ranked=sorted(count.items(),key=lambda x:x[1],reverse=True) #给dict排序

.items()    #整个dict
.values()   #值
.keys()     #键

num[left],num[right]=num[right],num[left]   #

nums[:k]    #从开头取到下标 k 之前，也就是取前 k 个元素。
nums[::k]   #从头到尾，每隔 k 个位置取一个。

zip(s, t)   #把两个序列里相同位置的元素配成一对。