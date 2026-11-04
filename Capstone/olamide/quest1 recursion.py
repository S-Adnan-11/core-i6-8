def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)

"""A. Trace it (5 marks): Without running the code, trace total(4). 
List the calls in the order they begin, 
then show how the return values travel back."""

"""
total(4) =
4 + total(3) =
3 + total(2) =
2 + total(1) =
1"""


"""B. Find the problem (5 marks): What happens for total(0) and total(-3)? 
Rewrite the function so negative inputs raise ValueError and zero returns 0. 
State the behavior you chose for non-integer input."""

"""for total(0) and total(3) the function enters an infinite loop 
since n - 1 will never equal 1.
"""
def total_rewrite(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    return n + total(n-1)

"""C. Explain termination (5 marks): 
In your own words, distinguish the base case from the recursive case. 
Explain why each call must move toward a stopping condition. 
What failure occurs if the stopping condition is never reached?"""

"""The recursive case continues the loop. 
It causes the function to call itself again instead of returning.

The base case ends the loop.
It causes the function to return instead of calling itself again.

If the stopping condition is never reached the program enters an infinite loop"""



"""D. Code it (5 marks): Write countdown_sum(n), 
which recursively returns the sum of odd positive integers from n down to 1. 
Return 0 for n <= 0. 
Do not use loops, sum(), count(), or comprehensions.

Examples:
countdown_sum(5)  # 9: 5 + 3 + 1
countdown_sum(4)  # 4: 3 + 1
countdown_sum(1)  # 1
countdown_sum(0)  # 0"""

def countdown_sum(n: int) -> int:
    if n <= 0:
        return 0
    if n % 2:
        return n + countdown_sum(n-2)
    else:
        return n-1 + countdown_sum(n-3)



