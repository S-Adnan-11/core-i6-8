
# Given:
def announce(func):
   print("Decorator is running")
   
   def wrapper(*args, **kwargs):
       print("Before function")
       result = func(*args, **kwargs)
       print("After function")
       return result
   return wrapper

@announce
def multiply(a, b):
   print("Multiplying")
   return a * b

print("Program started")
answer = multiply(3, 4)
print("Answer:", answer)


"""
    Exact output:
    Decorator is running
    Program started
    Before function
    Multiplying
    After function
    Answer: 12
"""


# Why does this happen?
# This happens because decorators are applied when the function is defined, not when it is called.


"""
    multiply = announce(multiply)
    When Python executes announce(multiply), it immediately executes:
    print("Decorator is running")
    That happens before Python reaches:
    print("Program started")
    Later, when multiply(3, 4) is called, Python actually executes the wrapper.
"""

# B. Explain the parts

# 1. What does `@announce` do?
"""It passes the original function into the decorator and replaces
the original function name with the returned wrapper."""


# 2. What is `wrapper`?
"""It is an inner function that surrounds the original function.
It allows us to execute additional instructions before or after the original function runs.
"""
# 3. Why use `*args` and `kwargs`?
"""
They allow the wrapper to accept different numbers and types of arguments.
*args collects positional arguments into a tuple.
**kwargs collects keyword arguments into a dictionary."""


# 4. Why does returning `result` matter?
"""
    The wrapper must return the original function's result so that the caller receives the correct value.
    Without it, the wrapper returns None by default."""


# The bug
"""
    It calls the original function but does not return its result. 
    therefore, the output becomes None."""


"""Because Python automatically returns None when a function finishes without an explicit return statement."""

# Corrected wrapper:
# def wrapper(*args, **kwargs):
#     result = func(*args, **kwargs)
#     return result

"""Now the original result is passed back to the caller."""


# D. Implement `count_calls`
# Implementation:
def count_calls(func):
   calls = 0
   def wrapper(*args, **kwargs):
       nonlocal calls

       calls += 1
       result = func(*args, **kwargs)
       wrapper.call_count = calls
       return result
   wrapper.call_count = calls
   return wrapper

# Demonstration
@count_calls
def add(a, b):
   return a + b

print(add(2, 3))    #5
print(add(5, 5))    #10
print(add(10, 20))  #30

print("Total calls:", add.call_count)  #output = 3
