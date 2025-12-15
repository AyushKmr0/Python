# from hello import hello

# hello(4)

myList1 = [1, 2, 3]
myList2 = myList1
myList1 = 'hello'
myList1 = [1, 2, 3]

# print(myList1)
# print(myList2)

myList1[0] = 33
# print(myList1)
# print(myList2)



l1 = [1, 2, 3]
l2 = l1

print(l1)
print(l2)

l1[0] = 44
print(l1)
print(l2)



import random

print(random.random())
print(random.randint(1, 10))

l1 =  ['morning','afternoon', 'evening', 'night']
print(random.choice(l1))

random.shuffle(l1)
print(l1)




num = (0.1 + 0.1 + 0.1) - 0.3
print(num)

from decimal import Decimal

num = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(num)

num2 = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(num2)


from fractions import Fraction

myFra = Fraction(1, 7)
print(myFra)



# set 

set_one = {1, 2, 3, 4}
intersection = set_one & {1, 3}

print(intersection)


union = set_one | {1, 3, 6}
print(union)

dif = set_one - {1, 3, 6}
print(dif)

dict = set_one - {1, 2, 3, 4}
print(dict)

print(type({}))
print(type(set()))


# Boolean type

print(type(True))
print(True == 1)
print(True == 1)
print(True == 1)
print(False == 0)
print(True is 1)
