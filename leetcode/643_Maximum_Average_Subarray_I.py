# def find_max_average(nums,k):
#     average=float('-inf')
#     lens=len(nums)
#     for j in range(lens-k+1):
#         average_1=sum(nums[j:j+k])/k
#         if average_1>average:
#             average=average_1
#     return average

# print(find_max_average([1, 12, -5, -6, 50, 3], 4))   # 期望 12.75
# print(find_max_average([5], 1))                       # 期望 5.0
# print(find_max_average([-1], 1))                      # 期望 -1.0

def find_max_average(nums, k):
    lens = len(nums)
    total = sum(nums[:k])
    average = total / k

    for j in range(k, lens):
        total += nums[j] - nums[j - k]
        average = max(average, total / k)

    return average
print(find_max_average([1, 12, -5, -6, 50, 3], 4))   # 期望 12.75
print(find_max_average([5], 1))                       # 期望 5.0
print(find_max_average([-1], 1))                      # 期望 -1.0