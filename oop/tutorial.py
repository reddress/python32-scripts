import math

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return "hello"

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def h(self):
        return math.sqrt(self.r * self.r + self.i * self.i)
    
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
    
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
