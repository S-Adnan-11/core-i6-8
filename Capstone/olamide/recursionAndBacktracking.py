

"""Write digit_sum(n) that returns the sum of the digits of a non-negative integer, 
without converting it to a string or using loops.
"""

def digit_sum(n: int) -> int:
    if n < 0:
        return digit_sum(-n)
    if n < 10:
        return n
    last_digit = n % 10
    remaining_digits = n // 10
    return last_digit + digit_sum(remaining_digits)

# def digital_root(n: int) -> int:
#     if n < 10:
#         return n
#     last_digit = n % 10
#     remaining_digits = n // 10
#     dsum = last_digit + digital_root(remaining_digits)
#     if dsum < 10:
#         return dsum
#     else:
#         return digital_root(dsum)

def digital_root(n: int) -> int:
    droot = n % 9
    if not droot:
        droot = 9
    return droot

def digital_root(n: int) -> int:
    return ((n - 1) % 9) + 1

"""Write is_palindrome(s) that ignores case and non-alphanumeric characters. Don’t use s[::-1].
"""
# def is_palindrome(s: str) -> bool:
#     left = 0
#     right = len(s) - 1

#     if right <= left:
#         return True
    
#     # Ignore non-alphanumeric characters
#     while right > left:
#         if not s[left].isalnum():
#             left += 1
#         if not s[right].isalnum():
#             right -= 1
#         if s[left].isalnum() and s[right].isalnum():
#             break

#     # Return false if the characters aren't mirrored, ignoring case
#     if s[left].casefold() != s[right].casefold():
#         return False
    
#     return is_palindrome(s[left+1:right])

def is_palindrome(s: str, left: int = None, right: int = None) -> bool:
    if left == None:
        left = 0
    if right == None:
        right = len(s) - 1
    
    if right <= left:
        return True
    
    # Ignore non-alphanumeric characters
    while right > left:
        if not s[left].isalnum():
            left += 1
        if not s[right].isalnum():
            right -= 1
        if s[left].isalnum() and s[right].isalnum():
            break

    # Return false if the characters aren't mirrored, ignoring case
    if s[left].casefold() != s[right].casefold():
        return False
    
    return is_palindrome(s, left+1, right-1)
    
    
"""000, 001, 010, 011, 100, 101, 110, 111"""
"""Write binary_strings(n) that returns every binary string of length n."""
def binary_strings(n: int) -> list[str]:
    if n == 0:
        return [""]
    if n == 1:
        return["0", "1"]
    bs = binary_strings(n-1)
    pwr2 = len(bs)
    for i in range(pwr2):
        bs.append("1" + bs[i])
        bs[i] = "0" + bs[i]
    return bs

def binary_no_adjacent_ones(n: int) -> list[str]:
    if n == 0:
        return [""]
    if n == 1:
        return["0", "1"]
    bs = binary_no_adjacent_ones(n-1)
    pwr2 = len(bs)
    for i in range(pwr2):
        if bs[i][0] != "1":
            bs.append("1" + bs[i])
        bs[i] = "0" + bs[i]
    return bs

"""Write letter_case(s) that returns every string you can make by 
changing each letter to upper or lower case. 
Digits stay as they are.
"""

def letter_case(s: str, start: int = 0) -> list[str]:
    if start >= len(s):
        return [s]
    
    variants = letter_case(s, start+1)
    for v in variants[:]:
        if len(s) > 0 and v[start].isalpha():
            if v[start].isupper():
                new_variant = v[:start] + v[start].lower() + v[start+1:]
            else:
                new_variant = v[:start] + v[start].upper() + v[start+1:]
            variants.append(new_variant)
    
    return variants

def letter_case_no_even_upper(s: str, start: int = 0) -> list[str]:
    if start >= len(s):
        return [s]
    
    variants = letter_case(s, start+1)
    for v in variants[:]:
        if len(s) > 0 and v[start].isalpha():
            if v[start].isupper():
                new_variant = v[:start] + v[start].lower() + v[start+1:]
            else:
                new_variant = v[:start] + v[start].upper() + v[start+1:]

            # Count the upper case characters
            upper_count = 0
            for char in new_variant:
                if char.isupper():
                    upper_count += 1
                    
            # Append only the variants with odd number of upper case characters
            if upper_count % 2:
                variants.append(new_variant)
    
    return variants
        






if __name__ == "__main__":
    # print(digit_sum(0))      # 0
    # print(digit_sum(7))      # 7
    # print(digit_sum(-1234))   # 10
    # print(digit_sum(99999))  # 45
    # print(digital_root(56))
    # print(is_palindrome("racecar"))                          # True
    # print(is_palindrome("A man, a plan, a canal: Panama"))   # True
    # print(is_palindrome("hello"))                            # False
    # print(is_palindrome(""))                                 # True
    # print(binary_strings(0))  # [""]
    # print(binary_strings(1))  # ["0", "1"]
    # print(binary_strings(2))  # ["00", "01", "10", "11"]
    # print(binary_strings(3))
    # print(binary_strings(4))  # 16
    # print(binary_no_adjacent_ones(1))
    # print(binary_no_adjacent_ones(2))
    # print(binary_no_adjacent_ones(3))
    # print(binary_no_adjacent_ones(4))
    # print(letter_case(""))      # [""]
    # print(letter_case("12"))    # ["12"]
    # print(letter_case("3z4"))   # ["3z4", "3Z4"]
    # print(letter_case("a1b2"))  # ["a1b2", "a1B2", "A1b2", "A1B2"]  (order may vary)
    print(letter_case_no_even_upper("a1b2c3"))



