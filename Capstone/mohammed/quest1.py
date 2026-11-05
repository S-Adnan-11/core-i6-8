def total(n): 
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1: 
        return n
    return n + total(n - 1)

def countdown_sum(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + countdown_sum(n - 1)
    return countdown_sum(n - 1)


"""
total(4) = 4 + total(3)
total(3) = 3 + total(2)
total(2) = 2 + total(1)
total(1) = 1 

total(2) = 2 + 1 = 3 
total(3) = 3 + 3 = 6 
total(4) = 4 + total(3) = 10
"""

"""
countdown_sum(5) = 5 + countdownsum(4)
countdown_sum(4) = countdown_sum(3)
countdown_sum(3) = 3 + countdown_sum(2)
countdown_sum(2) = countdown_sum(1)
countdown_sum(1) = 1 + countdown_sum(0)
countdown_sum(0) = 0

countdown_sum(1) = 1 + 0 = 1
countdown_sum(2) = 1 
countdown_sum(3) = 3 + 1 = 4 
countdown_sum(4) = 4
coutdown_sum(5) = 5 + 4 = 9
"""
