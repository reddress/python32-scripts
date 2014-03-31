x = 50

def func(x):
    print('x is', x)
    x = 2
    print('changed local x to', x)

func(x) # 50, 2
print('x is still', x) #50
