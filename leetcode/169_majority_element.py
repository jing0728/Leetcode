def majority_element(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num in nums:
        if count[num]>len(nums)/2:
            return num
print(majority_element([3, 2, 3]))          # 期望 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 期望 2
print(majority_element([5]))                # 期望 5