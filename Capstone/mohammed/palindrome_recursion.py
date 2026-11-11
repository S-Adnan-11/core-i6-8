def recur_palindrome(str, left, right):
    if left >= right:
        return True
    if str[left].lower() == str[right].lower():
        return recur_palindrome(str, left + 1, right - 1)
    if not str[left].isalnum():
        return recur_palindrome(str, left + 1, right)
    if not str[right].isalnum():
        return recur_palindrome(str, left, right - 1)
    if str[left].lower() != str[right].lower():
        return False 

s = 'a d d   a'
left = 0 
right = len(s) - 1
print(recur_palindrome(s, left, right))
    