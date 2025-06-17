## Movie Ticket Pricing
## => Movie tickets are priced based on age: $12 for adult(18 and over), $8 for children. Everyone get a $2 discount on Wednesday.

userage = int(input("Enter your age: "))
day = "Wedensday"

price = 12 if userage >= 18 else 8

if day == "Wedensday":
    price -= 2

print("Ticket price for you is $",price)
