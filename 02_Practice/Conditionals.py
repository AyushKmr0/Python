## Age Group Categorization
## => Classify a person's age group: Child(< 13), Teenager(13 - 19), Adult(20 - 59), Senior(60 +).

##------------------------------------------------------------------------------------------------

# userage = int(input("Provide me an age: "))

# if userage < 13:
#     print("Child")
# elif userage < 20:
#     print("Teenager")
# elif userage < 60:
#     print("Adult")
# else:
#     print("Senior")










## Movie Ticket Pricing
## => Movie tickets are priced based on age: $12 for adult(18 and over), $8 for children. Everyone get a $2 discount on Wednesday.

##------------------------------------------------------------------------------------------------


# userage = int(input("Enter your age: "))
# day = "Wedensday"

# price = 12 if userage >= 18 else 8

# if day == "Wedensday":
#     price -= 2

# print("Ticket price for you is $",price)










## Grade Calculator
## => Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(bleow 60).

##------------------------------------------------------------------------------------------------


# userscore = int(input("Enter your Grade: "))

# if userscore > 100 or userscore < 0:
#     print("Please verify your score again!")
#     exit()
    

# if userscore >= 90:
#     grade = 'A'
# elif userscore >= 80:
#     grade = 'B'
# elif userscore >= 70:
#     grade = 'C'
# elif userscore >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# print("Grade: ", grade)










## Fruit Ripeness Checker
## => Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)

##------------------------------------------------------------------------------------------------


# fruit = 'BANANA'
# color = input('Fruit color: ').upper()

# if fruit == 'BANANA':
#     if color == 'GREEN':
#         print('Unripe')
#     elif color == 'YELLOW':
#         print('Ripe')
#     elif color == 'BROWN':
#         print('OverRipe')
# else:
#     print('Not Found')











## Weather Activity Suggestion
## => Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

##------------------------------------------------------------------------------------------------

# weather = input('How\'s the weather: ').upper()

# if weather == 'SUNNY':
#     activity = 'Go for a walk'
# elif weather == 'RAINY':
#     activity = 'Read a book'
# elif weather == 'SNOWY':
#     activity = 'Build a snowman'
# else:
#     print('NOT FOUND!')

# print(activity)










## Password Strength Checker
## => Check if a password is 'Weak', 'Medium', or 'Strong'. Criteria: <6 char (Weak), 6-10 char (Medium), > 10 (Strong)

##------------------------------------------------------------------------------------------------

# password = input("Password: ").strip()
# pass_len = len(password)
# if pass_len < 6:
#     strength = 'Weak'
# elif pass_len <= 10:
#     strength = 'Medium'
# else:
#     strength = 'Strong'

# print('Your password is:', strength)










## is Leap year or not ?

##------------------------------------------------------------------------------------------------

year = int(input("Year = "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year," is a leap year")
else:
    print(year,"is NOT a leap year")
