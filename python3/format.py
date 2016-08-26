name = 'Andrew'
age = 21

# https://www.python.org/dev/peps/pep-3101/
print('my name is {}. I have {} eyars'.format(name, age))
print('my name is {0}. I have {1} eyars'.format(name, age))
('my name is {name}. I have {age} eyars'.format(name = 'Andrew', age = 21))
print('my name is ' + name + '. I have ' + str(age) + ' eyars')