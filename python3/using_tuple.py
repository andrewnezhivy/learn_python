zoo = ('питон', 'слон', 'пингвин')

print('количество животных в зоопарке', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo

print('количество клеток в зоопарке', len(new_zoo))
print('все животные в зоопарке', len(new_zoo))
print('животные привезенные из старого зоопарка', new_zoo[2])
print('аоследние животные привезенные из старого зоопарка', new_zoo[2][2])
print('количество животных в новом зоопарке', len(new_zoo)-1+len(new_zoo[2]))
