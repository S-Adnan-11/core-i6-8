""" QUEST 1 — Recursion: Follow the Calls """
def total(n):
    if n < 0:
        raise ValueError
    if n==0:
        return 0
    if n == 1:
        return 1
    return n + total(n-1)

def countdown_sum(n):
    if n <=0:
        return 0
    n=n-1 if not n%2 else n
    if n == 1:
        return n + countdown_sum(n-2)

""" The base case is the condition that stops the function from running continuosly, the recursive case is the condition that keeps calling the function"""
