number = 23
running = True

while running:
    guess = int(input('please enter an integer: '))

    if guess == number:
        print('сongratulations, you guessed it')
        print('(although it did not win any prize)')

        running = False
    elif guess < number:
        print('no, a little more unknown number of')
    else:
        print('no, a little less unknown number of')
else:
    print('while loop completed')

print('completed')
