def announce(func):
    print("Decorator is running") 
    def wrapper(*args, **kwargs): 
        print("Before function") 
        result = func(*args, **kwargs)
        print("After function") 
        return result 
    return wrapper


def multiply(a, b): 
    print("Multiplying") 
    return a * b

answer = announce(multiply)

print(answer(4,3))
print(answer(2,3))

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper 


def add_two(a):
    return a + 2 

ans = count_calls(add_two)
print(ans(3))
print(ans(4))
print(ans(4))
print(f"Final call count: {ans.call_count}")
