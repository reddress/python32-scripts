def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
    
def total2(init=10, **kwargs):
    '''sum initial number

    and keyword arguments'''
    print(kwargs)
    count = init
    for key in kwargs:
        count += kwargs[key]
    return count

