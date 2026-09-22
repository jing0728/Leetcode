"""def topKFrequent(self, nums, k):
    count={}
    i=0
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return(sorted_count[:k])"""

def top_k_frequent(nums, k):
    count={}
    ans=[]
    for num in nums:
        count[num]=count.get(num,0)+1
    ranked=sorted(count.items(),key=lambda num:num[1],reverse=True)
    for num,frq in ranked[:k]:
        ans.append(num)
    return ans

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))          # 期望 [1, 2]
print(top_k_frequent([1], 1))                          # 期望 [1]
print(top_k_frequent([4, 4, 4, 6, 6, 6, 6, 5], 1))     # 期望 [6]