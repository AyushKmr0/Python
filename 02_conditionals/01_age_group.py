## Age Group Categorization
##  => Classify a person's age group: Child(< 13), Teenager(13 - 19), Adult(20 - 59), Senior(60 +).

userage = int(input("Provide me an age: "))

if userage < 13:
    print("Child")
elif userage < 20:
    print("Teenager")
elif userage < 60:
    print("Adult")
else:
    print("Senior")
