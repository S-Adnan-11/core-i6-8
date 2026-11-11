def digit_sum_recur(n):
    if n == 0:
        return n 
    else:
        return n % 10 + digit_sum_recur(n // 10)

print(digit_sum_recur(12345))