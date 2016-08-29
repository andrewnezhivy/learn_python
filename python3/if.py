number = 23
guess = int(input('please enter an integer: '))

if guess == number:
    print('сongratulations, you guessed it')
    print('(although it did not win any prize)')
elif guess < number:
    print('no, a little more unknown number of')
else:
    print('no, a little less unknown number of')

print('completed')
