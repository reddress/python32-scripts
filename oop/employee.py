class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("My name is", self.name)

class Grunt(Employee):
    def setSupervisor(self, s):
        self.supervisor = s
        s.addSub(self)
        
    def getSupervisor(self):
        return self.supervisor
    
class Supervisor(Employee):
    subemployees = []
    
    def addSub(self, sub):
        self.subemployees.append(sub)
        
s = Supervisor("Joe", 45)
g = Grunt("Bob", 22)
g.setSupervisor(s)
