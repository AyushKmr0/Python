## Timing Function Execution
## => Write a decorator that mesures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start:.2f} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    
# example_function(2)






## Debugging Function Calls
## => Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key} = {value}" for key, value in kwargs.items())
        print(f"calling: {func.__name__} with args: {args_value or "None"}, and kwargs: {kwargs_value or "None"}")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("Hello World!")

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
    
# hello()
# greet("ayush", greeting="Good Morning")







## Cache Return Values 
## => Implement a decorator that caches the reutrn values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(5, 3))
