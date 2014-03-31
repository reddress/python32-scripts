def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

a = 4
print(total(10, 1, 2, 3, a, veg = 50, fruit = 100))
