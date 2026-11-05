def count_calls(func):
    count=[]
    def wrapper(*args,**kwargs):
        count.append(1)
        result=func(*args,**kwargs)
        print(f"Calls:",len(count))
        return result
    return wrapper

# def announce(func):
#     print("Decorator is running")


#     def wrapper(*args, **kwargs):
#         print("Before function")
#         result = func(*args, **kwargs)
#         print("After function")
#         return result
    
#     return wrapper


def multiply(a, b):
    print("Multiplying")
    return a * b

multiply=count_calls(multiply)

print("Program started")
answer = multiply(1, 1)
print("Answer:", answer)
print()
answer = multiply(2, 2)
print("Answer:", answer)
print()

answer = multiply("a", 4)
print("Answer:", answer)
print()

"""
@annouce decorates the mutiply function 
such than each time mutilply is called
it makes mutiply to be annouce(multiply)
"""
