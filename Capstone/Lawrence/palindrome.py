def is_palindrome(s):
    def helper(left, right):
        if left >= right:
            return True
        if not s[left].isalnum():
            return helper(left + 1, right)
        if not s[right].isalnum():
            return helper(left, right - 1)
        if s[left].lower() != s[right].lower():
            return False
        return helper(left + 1, right - 1)
        
    return helper(0, len(s) - 1)

print(is_palindrome("racecar"))  # True
print(is_palindrome("was it a car or a cat I !saw"))  # True
print(is_palindrome("a man a plan a canal Panama"))  # True
print(is_palindrome("Dadk!"))  # False
print(is_palindrome("Hello"))  # False
print(is_palindrome(""))  # True