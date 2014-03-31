try:
    text = input('enter something --> ')
except EOFError:
    print('Y U NO press enter?')
except:
    print('Y U CTRL-C')
else:
    print('you entered', text)
    
