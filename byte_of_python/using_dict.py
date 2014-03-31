ab = { 'swaroop': 'swarrop@warop.ch',
       'larry': 'larry@wall.org',
       'matsu': 'matz@rubi',
       'spammer': 'spammer@hotmail'
       }

print('swaroops addr is', ab['swaroop'])

del ab['spammer']

print('there are {0} contacts in addr book'.format(len(ab)))

for name, address in ab.items():
    print('contact {0} at {1}'.format(name, address))

ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print('guidos addr is', ab['guido'])

for elem in ab.items():
    print(elem[0], elem[1])
    
    
    
