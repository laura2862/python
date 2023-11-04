
class Student(object):
    count=0
    def __init__(self,name,age,mobile):
        self.name=name
        self.age=age
        self.mobile=mobile
    def __str__(self):
        return f'{self.name} is {self.age} years old, mobile is {self.mobile}. '






