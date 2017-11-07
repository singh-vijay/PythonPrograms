'''
Sets is collection of items with no duplicates
'''

groceries = {'serial', 'milk', 'beans', 'butter', 'bananas', 'milk'}
''' Ignore items which are given twice'''
print(groceries)

if 'pizza' in groceries:
    print("you already have pizza!")
else:
    print("You need to add pizza!")