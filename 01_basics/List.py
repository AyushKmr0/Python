lang = ['Python', 'Java', 'JavaScript', 'Go']

print(lang)
print(lang[2])
print(lang[:2])

lang[3] = 'Rust'
print(lang)

# lang[1:2] = 'Swift'
# print(lang)

lang[1:2] = ['Swift']
print(lang)

lang[1:1] = ['test', 'test']
print(lang)

lang[1:3] = []
print(lang)


for l in lang:
    # print(l, end=', ')
    print(l)

if 'Java' in lang:
    print("I have Java")

else:
    print("I dont have Java")


print(lang.pop())
print(lang)

lang.remove('Swift')
print(lang)

lang.insert(1, 'Swift')
print(lang)

lang_copy = lang.copy()

lang_copy.append('Go')
print(lang_copy)
print(lang)


squared_num = [x**2 for x in range(10)]
print(squared_num)
