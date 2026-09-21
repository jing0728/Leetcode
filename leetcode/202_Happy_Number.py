def is_happy(n):
    seen = set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        total=0
        for i in str(n):
            total+=int(i)**2
        n=total
    return True

        


print(is_happy(19))
# 期望 True

print(is_happy(2))
# 期望 False

print(is_happy(1))
# 期望 True

print(is_happy(7))
# 期望 True