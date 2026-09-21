def topKFrequent(self, nums, k):
    count={}
    i=0
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return(sorted_count[:k])

