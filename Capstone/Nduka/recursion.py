def total(n):
    n=int(n)
    if n<1:
        raise ValueError("Number must be positive")
    if n==1:
        return 1
    return n + total(n-1)

print(total(2))
"""
B.  When total(0) or total(negative numbr) is called the result doesnt converge to a 
    base case and recursion continues until maximum recursion depth is exceeded

C.  Base case stops the recursion. Recursive case continues recursion and keeps
    converging till it gets to base case
"""

def countdown_sum(n):
    n=int(n)
    if n<=0:
        return 0
    if n==1:
        return 1
    k=n
    if n%2==0:
        k=n-1


    return k + countdown_sum(k-2)

print(countdown_sum(1998))



