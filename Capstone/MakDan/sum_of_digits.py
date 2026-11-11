def digit_sum(n: int) -> int:
    if n < 0:
        raise ValueError("Enter positive integer only")
    if n < 10:
        return n
    return n % 10 + digit_sum(n//10)

# Test
numbers = [
    0,
    7,
    1234,
    99999
]

for num in numbers:
    print(digit_sum(num))
    print()