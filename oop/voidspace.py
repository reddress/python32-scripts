# http://www.voidspace.org.uk/python/articles/OOP.shtml

def fn1():
    print("you chose 1")
def fn2():
    print("you chose 2")
def fn3():
    print("you chose 3")

switch = {
    'one': fn1,
    'two': fn2,
    'three': fn3,
    }

choice = input("Enter one, two or three: ")

try:
    result = switch[choice]
except KeyError:
    print("Didn't understand your choice")
else:
    result()
    
