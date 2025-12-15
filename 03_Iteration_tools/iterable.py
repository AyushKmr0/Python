# iteration tool (for, comprehension)  -- iter() -->   iterable Objects (lists, file)  --->  response (__next__)


print("Hello world")

username = 'ayush'
print(username)

# f = open('iterable.py')
# f.readline()

# for line in open('iterable.py'):
#     print(line, end="")

# while loop 
# f = open('iterable.py')
# while True :
#     line = f.readline()
#     if not line : break
#     print(line, end="")



# iter tools
myList = [1, 2, 3, 4]

i = iter(myList)

print(i)
print(i.__next__())
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
# print(i.__next__())

