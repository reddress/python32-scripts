number = 23
running = True

while running:
    guess = int(input('enter an integer: '))

    if guess == number:
        print('you guessed it')
        print('(but no prize)')
        running = False
    elif guess < number:
        print('No, it is a little higher')
    else:
        print('No, it is little lower')
else:
    print('the while loop is over')

print('Done')
