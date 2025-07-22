greet = "Good Morning"
first_char = greet[0]

print(first_char)

slice_greet = greet[0:5]
print(slice_greet)

print(greet.lower())
print(greet.upper())


greet = "   Good Morning   "
print(greet.strip())


greet = "Good Morning"
print(greet.replace("Morning", "Night"))
print(greet)


greet = "Morning, Afternoon, Evening, Night"
print(greet.split(", "))

greet = "Good Morning"
print(greet.find('Morning'))    # result -> 5
print(greet.find('morning'))    # result -> -1


greet = "Good Good Good Good Morning"
print(greet.count('Good'))


game = 'GTA'
time = 6

play = "I was playing {} from last {} hrs"
print(play.format(game, time))
print("length => ",len(game))

games_veriety = ["GTA", "PUBG", "Counter_Strike"]
print(games_veriety)

print(", ".join(games_veriety))

for letter in game:
    print(letter)

path = 'c:\\user\\pwd'
print(path)

path = r"c:\user\pwd"
print(path)


word = "Hello World"
print("Worldd" in word)
print("World" in word)



# num_list = "0123456789"
# print(num_list[:])
# print(num_list[:7])
# print(num_list[0:7:2])
# print(num_list[0:7:3])
