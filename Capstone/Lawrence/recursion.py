def total(n):
   if n == 1:
       return 1
   return n + total(n -1)
print(total(4))

# (A) Trace

"""
Step 1: Calls begin
When we call total(4):
total(4)
total(3)
total(2)
total(1)


Step 2: How return values travel back:

total(1) = 1
total(2) = 2 + total(1)
       = 2 + 1
       = 3

total(3) = 3 + total(2)
       = 3 + 3
       = 6

total(4) = 4 + total(3)
       = 4 + 6
       = 10

Call stack visualization
1.  Call total(4) — waits for total(3).
2.  Call total(3) — waits for total(2).
3.  Call total(2) — waits for total(1).
4.  Call total(1) — returns 1.
5.  total(2) returns 3.
6.  total(3) returns 6.
7.  total(4) returns 10.
"""

# (B). Find the problem
"""
The original function has a problem with zero and negative numbers.
For total(0);
The function keeps decreasing. It never reaches n == 1.
The same happens with total(-3).
Eventually, Python raises RecursionError: maximum recursion depth exceeded
"""
# Corrected implementation:
def total(n):
   try:
       if not isinstance(n, int):
           raise TypeError("Input must be an integer")
  
       if n < 0:
           raise ValueError("Input cannot be nagative")
   except (ValueError, TypeError) as e:
           return e
      
   if n == 0:
       return 0
   if n == 1:
       return 1
   return n + total(n - 1)


# Test cases:
print(total(4))  # 10
print(total(1))  # 1
print(total(0))  # 0
print(total(5)) #15
# Edge cases:
print(total(-3))   # Raises ValueError
print(total(2.5))  # Raises TypeError
print(total("5"))  # Raises TypeError


"""Decision:
Negative integers raise ValueError because the input has the
correct type but is outside the permitted range.
Non-integers raise TypeError because the function requires an integer.
"""


# (C) Base case and Recursive case:
"""
1. Base case;
The base case is the condition that stops recursion.
When the function reaches this condition, it returns a value without making another recursive call.


2. Recursive case;
The recursive case is where the function calls itself with a smaller or simpler task.


Why each call must move towards the base case;
Because without progress, the function will continue calling itself indefinitely.

The argument never changes, so the base case is never reached.
Python eventually raises a RecursionError because the call stack becomes too deep."""




# (D). Recursively Return the sum of odd positive integers from n down to 1.

def countdown_sum(n):
   if n <= 0:
       return 0
   if n % 2 == 0:
       return countdown_sum(n - 1)
   return n + countdown_sum(n - 2)


"""Test cases"""


print(countdown_sum(5))     # 9
print(countdown_sum(4))     # 4
print(countdown_sum(1))     # 1
print(countdown_sum(0))     # 0
print(countdown_sum(-3))    # 0
print(countdown_sum(8))     # 16


"""Trace of (5):
countdown_sum(5)
= 5 + countdown_sum(3)
= 5 + 3 + countdown_sum(1)
= 5 + 3 + 1 + countdown_sum(-1)
= 5 + 3 + 1 + 0
= 9
"""