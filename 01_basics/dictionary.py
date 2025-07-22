capitals = {"India":"Delhi", "Gujarat":"Gandhinagar",  "Karnataka":"Bengaluru", "Jharkhand":"Ranchi", "Telangana":"Hyderabad"}


print(capitals.get('Gujarat'))
capitals["India"] = "Kolkata"
print(capitals)

for cap in capitals:
    print(cap, ':', capitals[cap])

for key, values in capitals.items():
    print(key, ':', values)

if 'India' in capitals:
    print('I\'m from India')

print(len(capitals))

capitals["Maharashtra"] = "Mumbai"
print(capitals)

capitals.pop('Maharashtra')
print(capitals)

capitals.popitem()
print(capitals)

del capitals['Karnataka']   # delete the reference from memory
print(capitals)




# { {}, {}, {} }
print("\n.....................................................\n")
tea_shop = {
    "Chai": {"Masala":"Spicy", "Ginger":"Zesty"},
    "Tea": {"Green":"Mild", "Black":"Strong"},
}

print(tea_shop['Chai'])
print(tea_shop['Chai']['Ginger'])

squared_num = {x:x**2 for x in range(5)}
print(squared_num)

squared_num.clear()
print(squared_num)


print("\n.....................................................\n")

keys = ['1', '2', '3', '4']
default_value = 'Number'

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
