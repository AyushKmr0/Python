username = 'ayush'

# def func() :
#     # username = 'yeash'
#     print(username)

# print(username)
# func()



x = 99

# def func2(y) :
#     z = x + y
#     return z

# result = func2(1)
# print(result)




# def func3() :
#     global x
#     x = 33
    
# func3()
# print(x)




# def f1() :
#     x = 88
#     def f2():
#         print(x)
    
#     return f2
    
# result = f1()
# result()




def function(num) :
    def actual_fun(x) :
        return x ** num
    return actual_fun

f = function(2)
g = function(3)

print(f(3))
print(g(3))
