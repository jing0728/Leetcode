def max_area(height):
    left=0
    right=len(height)-1
    ans=set()
    while left<right:
        area=min(height[left],height[right])*(right-left)
        ans.add(area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max(ans)
print(max_area([1,8,6,2,5,4,8,3,7]))
# 期望 49

print(max_area([1,1]))
# 期望 1

print(max_area([4,3,2,1,4]))
# 期望 16

print(max_area([1,2,1]))
# 期望 2