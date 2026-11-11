def digit_sum(n):
    if n < 10:
        return n
    
    digit = n % 10
    n = n // 10
    return digit + digit_sum(n)

# print(digit_sum(0))
# print(digit_sum(7))
# print(digit_sum(1234))
# print(digit_sum(99999))

def digital_root(n):
    if n < 10:
        return n

    # If you want to use the digit_sum() above
    # n = digit_sum(n)

    # If you don't want to use the digit_sum() above
    n = (n % 10) + (n // 10)
    
    return digital_root(n)

print(digital_root(942))

def digit_sum2(n):
    n = abs(n)

    if n // 10 == 0:
        return n

    digit = n % 10
    n = n // 10

    return digit + digit_sum2(n)

# print(digit_sum2(-0))
# print(digit_sum2(-7))
# print(digit_sum2(-1234))
# print(digit_sum2(-99999))