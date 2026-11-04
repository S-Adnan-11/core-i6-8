""" Quest 4 - Decorators """

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

def count_calls(func):
    count = 0
    def counter(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{count} counts")
        result = func(*args, **kwargs)
        return result
    return counter

@count_calls
def multiply(a, b):
    print("Multiplying")
    return a * b

print("Program started")
answer = multiply(3, 4)
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))
print("Answer:", answer)


"""Decorator is running
Program started
1 counts
Multiplying
2 counts
Multiplying
6
3 counts
Multiplying
20
4 counts
Multiplying
42
Answer: 12"""