class Robot:
    '''Represents a robot with a name'''

    # a class variable
    population = 0

    def __init__(self, name):
        '''initializes data'''
        self.name = name
        print('(Initializing {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{0} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('there are still {0:d} robots working'.format(Robot.population))

    def sayHi(self):
        print('I am {0}'.format(self.name))

    @staticmethod
    def howMany():
        print('population:', Robot.population)

    #howMany = staticmethod(howMany)

droid1 = Robot('r2d2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('c3po')
droid2.sayHi()
Robot.howMany()

del droid1
del droid2

Robot.howMany()
                  
