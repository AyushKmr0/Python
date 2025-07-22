## Counting Positive Number
## => Count how many positive numbers in the list =  [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

##------------------------------------------------------------------------------------------------

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# isPositive_count = 0

# for num in numbers:
#     if num > 0:
#         isPositive_count += 1

# print('Final count of Positive number is:', isPositive_count)










## Sum of Even Numbers
## => Calcualte the sum of even numbers up to a given number n.

##------------------------------------------------------------------------------------------------


# number = int(input("Number: "))
# sum_even = 0

# for num in range(1, number + 1) :
#     if num % 2 == 0:
#         sum_even += num

# print("The sum of even numbers up to a given number",number, "is :", sum_even)










## Reverse a String

##------------------------------------------------------------------------------------------------

# str = input("String : ")
# reversed_str = ''

# for char in str:
#     reversed_str = char + reversed_str

# print(reversed_str)









## Find the first non-repeated character

##------------------------------------------------------------------------------------------------

# input = 'teeterabcabc'
# char = '' 

# for c in input:
#     if input.count(c) == 1:
#         char += c
#         break

# print("The first non-repeated character is:",char)










## Validate Input
## => Keep asking the user for input until they enter a number between 1 and 10.

##------------------------------------------------------------------------------------------------

# while True :
#     number = int(input("Enter a number b/w 1 to 10: "))
#     if 1 <= number <= 10 :
#         print("Got it")
#         break
#     else:
#         print('Invalid number, try again')










## Prime number checker

##------------------------------------------------------------------------------------------------

# number = int(input("Enter a number: "))
# is_prime = True

# if number > 1:
#     for i in range(2, number) :
#         if (number % 2) == 0 :
#             is_prime = False
#             break

# print(is_prime)










## List uniqueness checker
## => Check if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate

items = ["apple", "banana", "orange", "apple", "mango"]

unique_list = set()

for item in items:
    if item in unique_list:
        print('Duplicate')
        break

    unique_list.add(item)










## Exponential Backoff
## => Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stop after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print('Attempts', attempts + 1, '-wait time', wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
