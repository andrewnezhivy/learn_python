while True:
    s = input('enter something: ')

    if s == 'exit':
        break
    print('length of string:', len(s))

    if len(s) < 3:
        print('too few')
        continue

    print('entered string a sufficient length')
