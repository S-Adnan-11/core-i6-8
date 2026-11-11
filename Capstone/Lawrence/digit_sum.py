

def digit_sum(n):
    if n < 0:
        raise ValueError("num must be a non-negative integer")
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(123456))


def negative_digit_sum(n):
    if n < -9:
        return -n % 10 + negative_digit_sum(-(-n // 10))
    if n < 0:
        return -n
    if n > 9:
        return n % 10 + negative_digit_sum(n // 10)
    return n

print(negative_digit_sum(-123456))
print(negative_digit_sum(123456))


def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def digital_root(n):
    """Write digital_root(n), which keeps summing digits until one digit remains (942 → 15 → 6)"""
    n = digit_sum(n)
    if n < 10:
        return n
    return digital_root(n)

print(digital_root(942))  # 6
print(digital_root(-123))  # 6