classMate = {'Tony':'Iron Man', 'Bucky':'Winter Soldier', 'Natasha':'Black Widow', 'Roger':'Captain America', 'Banner':'Hulk', 'Shaktimaan':'Gangadhar'}

print('Printing the Dictionary')
print(classMate)

print('Printing the value for Tony and Natasha')
print(classMate['Tony'])
print(classMate['Natasha'])

print('\nPrinting complete dictionary with the values !!\n')
for k, v in classMate.items():
    print(k, "is", v)