def digit_sum(n: int) -> int:
    if n < 0:
        raise ValueError("Enter positive integer only")
    if n < 10:
        return n
    return n % 10 + digit_sum(n//10)

def digital_root(n):
    if n < 0:
        raise ValueError("Enter positive integer only")
    if n < 10:
        return n
    n = n % 10 + digital_root(n//10)
    return n%9 if n%9 else 9
    


# Test
numbers = [
    0,
    7,
    1234,
    99999,
    942
]

for num in numbers:
    print(digit_sum(num))
    print(digital_root(num))
    print()