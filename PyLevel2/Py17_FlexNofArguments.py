def addNumbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

addNumbers(1)
addNumbers(3, 32)
addNumbers(3, 5, 7, 16)
