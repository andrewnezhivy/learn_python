def printMax(a, b):
    if a > b:
        print(a, 'is the maximum')
    elif a == b:
        print(a, 'equals', b)
    else:
        print(b, 'is the maximum')

printMax(3, 4)

x = 5
y = 7

printMax(x, y)
printMax(y, x)
