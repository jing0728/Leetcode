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
''.join(...)  #把多个字符串拼起来。

filter()    #从一堆东西里面，把满足条件的留下来。
filter(判断函数, 要遍历的数据)

遍历list：
for num in nums:
    print(num)

遍历list带下标：
for i,num in enumerate(nums):
    print(i,num)

dict统计次数：
count={}
for num in nums:
    count[num]=count.get(num,0)+1   # dict.get(key,默认值)

set查重复：
seen=set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)

dict存下标：
seen={}
for i,num in enumerate(nums):
    seen[num]=i

split
s="dog cat cat dog"
word=s.split()
#["dog", "cat", "cat", "dog"]

join
letter=["a","b","c"]
"".join(letters)
#"abc"

字符串反转
"hello"[::-1]
#olleh

list切片
num[:k] #前k个
num[:k] #从k到结尾
num[::-1]   #反转
num[::2]    #每隔2个取一个

sorted
sorted(nums)
sorted(nums,reverse=True)   #从大到小
sorted(nums,reverse=False)  #从小到大

按dict value排序
sorted(dict.items(),key=labdm x:x[1],reverse=True)
x[0]    #key
x[1]    #value

d.keys()
d.values()
d.items()

zip
for a,b in zip(a,b):
    print(a,b)

双指针
left=0
ritght=len(nums)-1
while left<right:
    ...
    left+=1
    right-=1

交换两个值
nums[left],num[right]=num[right],num[left]

list添加和删除
nums.append(x)
nums.pop()
nums.pop(i)
nums.remove(x)

原地排序/反转 #不创建新的list
nums.sort()
nums.reverse()

filter
filter(function,iserable)

map
map(function, iterable)

列表推导式
[list(x) for x in ans]  #把 ans 里面的每一个 x 都拿出来，做一次 list(x)，然后把结果组成一个新的 list。

i,num in enumerate(nums) #i在前面num在后才可以

lst = [1, 2, 3]
lst.append(4)       # 末尾加一个：[1, 2, 3, 4]
lst.insert(0, 0)    # 指定位置插入：[0, 1, 2, 3, 4]
lst.remove(2)        # 删掉值为2的那个（第一个匹配的）
lst.pop()             # 删掉最后一个并返回它
lst.pop(0)            # 删掉指定位置的

s = set()
s.add(1)           # 加一个
s.add(1)           # 重复加同一个，没有效果，还是只有一个
s.remove(1)          # 删掉指定的

d = {}
d["a"] = 1       # 没有 "a" 这个键 → 新增
d["a"] = 2       # 已经有 "a" 这个键 → 覆盖原来的值
del d["a"]        # 删掉这一对