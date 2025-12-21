x = ('superman', 'batman', 'ironman')
y = enumerate(x, start=1)

print(y)

li = list(y)
print(li)


# file = open('test.py')
file = open('test.py', 'w')

try:
    file.write("Hello World!")
finally:
    file.close()
    
# ---------------------------------------

with open('youtube.txt', 'w') as file:
    file.write("Hello World!")
