## Age Group Categorization
##  => Classify a person's age group: Child(< 13), Teenager(13 - 19), Adult(20 - 59), Senior(60 +).

# age = int(input('Enter your age: '))

# if age < 0:
#     print('Enter a valid age!')
#     exit()

# if age < 13 :
#     print('Child')
# elif age >= 13 and age <= 19:
#     print('Teenager')
# elif age >=20 and age <=59:
#     print('Adult')
# elif age >= 60:
#     print("Senior")




## Movie Ticket Pricing
## => Movie tickets are priced based on age: $12 for adult(18 and over), $8 for children. Everyone get a $2 discount on Wednesday.


# age = int(input("Enter your age: "))
# wednesday = True

# price = 12 if age >= 18 else 8

# if wednesday:
#     price -= 2

# print("Movie Ticket Price: $",price)



## Grade Calculator
## => Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(bleow 60).

score = int(input("Enter score: "))

if score > 100 or score < 0:
    print('Enter a valid score!')
    exit()

if score >= 90 :
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Your Grade is : ',grade);
