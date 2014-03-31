class SchoolMember:
    '''represents a school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('initialzied schoolmember: {0}'.format(self.name))

    def tell(self):
        '''tell my details'''
        print('Name: {0}, age: {1}'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('initialized teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('initialized student', self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {0:d}'.format(self.marks))

t = Teacher('Mrs Shiv', 40, 30000)
s = Student('Swaroop', 25, 79)

members = [t, s]
for member in members:
    member.tell()
              
