##########
# QUEST 4 — Decorators
##########

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

### A. Predict the output: Write every printed line in exact order before running the program. Explain why the decorator's first print happens before “Program started.”

  # Expected output:
  # Decorator is running
  # Program started
  # Before function
  # Multiplying
  # After function
  # Answer: 12

  # The decorator's first print happens before “Program started” because the `@announce` decorator is applied to the `multiply` function at definition time. When the Python interpreter encounters the `@announce` decorator, it immediately calls the `announce` function with `multiply` as an argument, and the print statement inside `announce` executes right away.

### B. Explain the parts: What does @announce do? What is wrapper? Why are *args and **kwargs useful? Why does returning result matter?

  # The @announce tells Python to pass the multiply function into the announce decorator.

  # The wrapper is an inner function defined inside the decorator. Its job is to wrap additional behavior around the original function.

  # *args and **kwargs are useful because they allow the wrapper function to accept any number of positional and keyword arguments, making it flexible enough without needing to know the exact parameters of the function being decorated.

  # Returning `result` from the `wrapper` function is important because it allows the modified function to return the same value as the original function. If we didn't return `result`, the caller of the decorated function would not receive the expected output, which could lead to unexpected behavior in the program.

### C. Repair a bug: If wrapper calls func(*args, **kwargs) but does not return its result, answer becomes None. Explain why and correct the wrapper.

  # If the wrapper calls func(*args, **kwargs) but does not return its result, the decorated function will return None because the wrapper function itself does not have a return statement. In Python, if a function does not explicitly return a value, it implicitly returns None.

  # To correct the wrapper, we need to ensure that it returns the result of the original function call. The corrected wrapper should look like this:
    # def wrapper(*args, **kwargs):
    #     print("Before function")
    #     result = func(*args, **kwargs)
    #     print("After function")
    #     return result  # Ensure the result is returned to the caller

###. D. Implement: Write count_calls, a decorator that tracks how many times a decorated function is called. The count must persist, the original result must be returned, and positional arguments must work. Demonstrate three calls and show the final count

def count_calls(func):
    count = 0  # Initialize a counter

    def wrapper(*args, **kwargs):
        nonlocal count  # Use nonlocal to modify the count variable
        count += 1  # Increment the count each time the function is called
        result = func(*args, **kwargs)  # Call the original function
        return result  # Return the result of the original function

    def get_count():  
        return count  # Return the current count
    wrapper.get_count = get_count  # Attach the get_count function to the wrapper
    return wrapper

@count_calls
def multiply(a, b):
    return a * b

# Demonstrate three calls
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))

# Display the final count
print("Total function calls:", multiply.get_count())