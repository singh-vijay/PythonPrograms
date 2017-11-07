# continue example
numTaken = [7, 9, 11, 15, 17]

print('Here are numbers still available')
for n in range(1, 20):
    if n in numTaken:
        continue
    else:
        print(n)
