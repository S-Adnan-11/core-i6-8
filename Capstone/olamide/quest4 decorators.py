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


"""A. Predict output (5 marks): 
Write every printed line in exact order before running the program. 
Explain why the decorator's first print happens before “Program started.”"""

"""
Decorator is running
Program started
Before function
Multiplying
After function
Answer: 12

When the @announce decoration is called python runs the announce function
and receives the returned output, wrappper.
Essentially:

wrapper = announce(multiply)

and then:

multiply = wrapper

In one line:

multiply = announce(multiply)

Everything happens after that.
So the announce function is called before print("Program Started")
"""

"""B. Explain the parts (5 marks): 
What does @announce do? 
What is wrapper? 
Why are *args and **kwargs useful? 
Why does returning result matter?"""

"""
*args represent a sequence/list of positional arguments
**kwargs represent a sequence/dictionary of keyword arguments

Without returning the result wrapper would return none making
it a poor wrapper for the function since it would stifle the output.
"""

"""D. Implement (5 marks): 
Write count_calls, a decorator that tracks how many times a 
decorated function is called. 
The count must persist, 
the original result must be returned, 
and positional arguments must work. 
Demonstrate three calls and show the final count."""

def count_call(func: function):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        print(f"Used {func.__name__} {count} times")
        return result
    return wrapper

@count_call
def chai():
    return "Chai!"

if __name__ == "__main__":
    print(chai())
    print(chai())
    print(chai())


