ab = {'swaroop': 'swaroop@swaroop.com',
      'larry': 'larry@wall.com',
      'matsumoto': 'matx@ruby-lang.org',
      'stammer': 'stammer@hotmail.com'
      }

print("адрес Swaroop'а", ab['swaroop'])

del ab['stammer']
print('в адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('контакт {0} с адресом {1}'.format(name, address))

ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print('адрес Guido', ab['guido'])
