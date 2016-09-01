def print_max(x, y):
    """Выводит максимальное значение двух чисел.

    Оба значения болжны быть целыми числами"""

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


print_max(3, 5)

print(print_max.__doc__)

help(print_max)

# об аннотациях функций
# https://www.python.org/dev/peps/pep-3107/
