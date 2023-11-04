class Tools(object):
    count =0
    def __init__(self,name):
        self.name = name
        Tools.count+=1
    @classmethod
    def getCount(cls):
        return Tools.count
class Ax(Tools):pass
class Knife(Tools):pass

t1=Ax('ax')
t2=Knife('knife')
print(Tools.getCount())
print(Ax.getCount())
print(t1.getCount())


