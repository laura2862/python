


class House():
    def __init__(self,area,addr):
        self.area=area
        self.__addr=addr
        self.containItems=[]
    def __str__(self):
        msg=f'this house located in {self.addr}, it has {self.area} squar meters left, and it contains: '
        if len(self.containItems) >0:
            for i in self.containItems:
                msg+= i.getName() +','
            msg=msg.strip(',')
            msg=msg.strip(',')
            msg=msg.strip(',')
            msg=msg.strip(',')
        else:
            msg+='none item'
        return msg
    def addItem(self,item):
        iarea=item.getArea()
        if self.area >= iarea:
            self.containItems.append(item)
            self.area-=iarea

            print(f'added item {item.getName()}, and left {self.area} squar meters!!!')
        else:
            print('can not be added!!!')
class Bed():
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        msg=f'{self.name} takes {self.area} squar meters!!!'
        return msg
    def getArea(self):
        return self.area
    def getName(self):
        return self.name

if __name__ == '__main__':
    bed1=Bed('bed1',30)
    bed2 = Bed('bed2', 30)
    house=House(100,'1 rd,nanjing')
    print(house)
    house.addItem(bed1)
    house.addItem(bed2)
    print(house)
    print(house._House__addr)


