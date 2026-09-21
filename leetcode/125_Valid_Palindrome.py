def is_palindrome(s):
    clean = ''.join(filter(str.isalnum, s)).lower()
    return clean == clean[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
# 期望 True

print(is_palindrome("race a car"))
# 期望 False

print(is_palindrome(" "))
# 期望 True

print(is_palindrome("0P"))
# 期望 False