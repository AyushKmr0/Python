## Grade Calculator
## => Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(bleow 60).

userscore = int(input("Enter your Grade: "))

if userscore >= 101:
    print("Please verify your score again!")
    exit()
    

if userscore >= 90:
    grade = 'A'
elif userscore >= 80:
    grade = 'B'
elif userscore >= 70:
    grade = 'C'
elif userscore >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade: ", grade)
