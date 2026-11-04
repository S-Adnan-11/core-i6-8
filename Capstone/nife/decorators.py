def announce(func):
    print("Decorator is running")

    def wrapper(*args, **kwargs):    # collecting arguments into a function
        print("Before function")
        result = func(*args, **kwargs)  # unpacking arguments when calling a function
        print("After function")
        return result

    return wrapper

# args without the * returns the arguments as a tuple rather than unpacking them which could lead to an error
# kwargs without the ** returns the arguments as a dictionary rather than unpacking them which could lead to an error

@announce
def multiply(a, b):
    print("Multiplying")
    return a * b

print("Program started")
answer = multiply(3, 4)
print("Answer:", answer)

def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function called {count} time(s)")
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_calls
def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))

# Decorator is running
# program started
# before function
# multiplying
# after function

# A. printed lines in order

# Decorator is running  1
# Before function   3
# After function    5
# Multiplying   4
# Program started   2

# Write every printed line in exact order before running the program. Explain why the decorator's first print happens before “Program started.”
# Because the decorator runs first so the print function in it runs and then the wrapper function is returned to announce

# B
# @announce decorates the function multiply, *args and **kwargs are important for collecting arguments into warpper funtion so the function being called can take arguments and also for unpacking arguments when the function is called, returning result is important so the wrapper function would not return None 

# C
# Without returning result, answer becomes None because when the function was called, the output was stored in the result variable but result wasn't returned, hence None becomes the output. To correct it, result should be returned