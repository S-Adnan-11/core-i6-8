import string

def digit_sum(n):
    if n < 0:
        raise ValueError("make it a non-negative integer.")
    elif n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)


print(digit_sum(1)) 



def palindrome(s):

    sentence = s.translate(str.maketrans('', '', '.,:;!? ')).lower().strip()

    left = 0
    right = len(sentence) - 1

    while left < right:
        if sentence[left] != sentence[right]:
            return False
            break
        left += 1
        right -= 1
        
    return True

print(palindrome("A man, a plan, a canal: Panama"))


def binary_strings(n):
    res = []

    def backtrack(current, binary):
        if len(current) == n:
            res.append("".join(current))
            return
        for x in binary:
            current.append(x)
            backtrack(current, binary)
            current.pop()

    backtrack([], ["0", "1"])
    return res
            



print(binary_strings(3))
        
