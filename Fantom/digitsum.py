def digit_sum(n):
    if n <= 9:
        return n
    last = n % 10
    rest = n // 10
    return last + digit_sum(rest)
print(digit_sum(1234))