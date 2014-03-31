class Person:
    def __init__(self, n):
        self.name = n
    def sayHi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.sayHi()
