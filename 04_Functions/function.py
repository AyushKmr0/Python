## Basic function syntax and return the square of a number

# def square(number) :
#     return number ** 2

# result = square(4)
# print(result)










## Function with multiple parameters
## => Create a function that takes two numbers as parameters and returs their sum.

# def sum_of_two(num1, num2) :
#     return num1 + num2

# print(sum_of_two(4, 5))










## Polymorphism in functions
## => WAF 'multiply' that multiplies two numbers, but can also accept and multiply strings.

# def multiply(val1, val2) :
#     return val1 * val2

# print(multiply(4, 4))
# print(multiply('ayush', 4))
# print(multiply(4, 'ayush'))










## Function returning multiple values
## => Create a function that returns both the area and circumference of a circle given its radius.

# import math

# def circle_stats(radius) :
#     area = math.pi * radius ** 2
#     circum = 2 * math.pi * radius

#     return area, circum

# area, circum = circle_stats(2)
# print(f'Area: {area:.2f}')
# print(f'Circumference: {circum:.2f}')










## Default parameter value
## => WAF that greets a user. if no name is provided, it should greet with adefault name.

# def greet(name = 'user') :
#     return "Hello, " + name + "!"

# print(greet('ayush'))
# print(greet())










## Lambda function
## => Create a lambda function to compute the cube of a number

# cube = lambda x: x ** 3

# print(cube(3))



## Functino with *args
## => Write a funciton that takes variable number of argumnts and return their sum

# def sum_of_all(*args) :
#     print(*args)
#     print(args)
#     # return sum(args)
    
#     sum = 0
#     for i in args:
#         sum += i
        
#     return sum

# print(sum_of_all(1, 2, 3))
# print(sum_of_all(1, 2, 3, 4, 5))
# print(sum_of_all(1, 2, 3, 4, 5, 6, 7))



## Function with **kwargs
## => Create a function that accepts any number of keyword arguments and prints them in the format key: value

def print_kwargs(**kwargs) :
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        

# print_kwargs(name="Shaktiman", power="lazer")
# print_kwargs(name="Shaktiman")
# print_kwargs(name="Shaktiman", power="lazer", enemy="Dr. Jackaal")




## Generate a function with yield
## => Write a generator function that yields even numbers up to a specified limit.

# def even_generator(limit) :
#     for i in range(2, limit + 1, 2):
#         yield i
        
# for num in even_generator(10) :
#     print(num)
    
    
    

## Recursive Function
## => Create a recursive function to calculate the factorial of a number.

def factorial(num) :
    if(num <= 0) :
        return 1
        
    return num * factorial(num - 1)
        
print(factorial(4))
