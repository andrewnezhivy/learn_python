def print_max(a, b):
    if a > b:
        print(a, 'is the maximum')
    elif a == b:
        print(a, 'equals', b)
    else:
        print(b, 'is the maximum')


print_max(3, 4)

x = 5
y = 7

print_max(x, y)
print_max(y, x)
