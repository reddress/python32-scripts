number = 23
guess = int(input('enter an integer: '))

if guess == number:
    print('you guessed it')
    print('(but no prize)')
elif guess < number:
    print('No, it is a little higher')
else:
    print('No, it is little lower')

print('Done')
