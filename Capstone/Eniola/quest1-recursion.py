##########
# QUEST 1 - Recursion
##########

def total(n): 
  if n == 1: 
    return 1 
  return n + total(n - 1)

### A. Trace it - total(4)
# total(4) = 4 + total(3)
# total(3) = 3 + total(2)
# total(2) = 2 + total(1)
# total(1) = 1
# Therefore, total(4) = 4 + 3 + 2 + 1 = 10

### B. Find the problem - What happens for total(0) and total(-3)?
# For total(0): The function will not terminate because there is no base case for n == 0.
# For total(-3): The function will not terminate because there is no base case for n < 1.

def total_new(n): 
  if n == 0 or n == 1: 
    return n
  if type(n) is not int:
    raise TypeError("Input must be an integer.") # The behaviour I chose for non-integer inputs is to raise a TypeError.
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  return n + total_new(n - 1)

### C. Explain termination
# The base case in the function is when n is 0 or 1. When n reaches 0 or 1, the function returns n, which stops the recursion. If n is negative or not an integer, the function raises an error, preventing infinite recursion.
# The recursive case is when n is greater than 1. In this case, the function calls itself with n - 1, which continues until it reaches the base case.
# Each call must move toward a stopping condition because n is decremented by 1 in each recursive call. This ensures that the function will eventually reach the base case and terminate.
# The failure that occurs if the stopping condition is never reached is an infinite recursion, which would lead to a stack overflow error.

### D. Code it
def countdown_sum(n): 
  if n <= 0: 
    return 0
  if n % 2 == 0:
    n -= 1 
  return n + countdown_sum(n - 2)

print(countdown_sum(5)) # 9
print(countdown_sum(4)) # 4
print(countdown_sum(1)) # 1
print(countdown_sum(0)) # 0