while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if s == 'help':
        print('type a string')
        print('type quit to quit')
    print('length of string is', len(s))
print('Done')
