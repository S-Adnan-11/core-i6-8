def total(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('Negative not allowed')
    return n + total(n-1)
        
print(total(2))

def countdown(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    if n%2 == 0:
        return (n-1) + countdown(n-3)
    return n + countdown(n-2)

# print(countdown(5))

def sum_down(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    return n + sum_down(n-1)

def count(n):
    if n//10 == 0:
        return 1
    return 1 + count(n // 10 )

# print(count(567))

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

# print(power(2, 3))


def sum_digits(n):
    if n == 0:
        return 0
    if n//10 == 0:
        return n
    return n%10 + sum_digits(n//10)

# print(sum_digits(1234))