lang = ('C', 'C++', 'Java', 'JavaScript')

print(lang[2])


# lang[1] = 'Python' -> - tuple is immutable, - fixed in the memory, - references can be changed but the existing one will not be changed
# print(lang) 

more_lang = ('Python', 'Go')

all_lang = lang + more_lang
print(all_lang)

if 'Python' in all_lang:
    print('Learing Python')

more_lang = ('Python', 'Go', 'Python')
print(more_lang.count('Python'))


(c, cpp, java, js) = lang

print(c)
print(cpp)
print(java)
print(js)

print(type(c))

# nested tuple is allowed -> ("", (1, 2, 3), "")
