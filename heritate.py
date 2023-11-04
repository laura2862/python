class Dog(object):
    def work(self):
        print(' basic class dog barking to every objects!!!')
class drugDog(Dog):
    def work(self):
        print(' derivative class dog of drug dog barking to drug dealers~~~')
class armyDog(Dog):
    def work(self):
        print(' derivative class dog of army dog barking to robbers~~~')
class Person(object):
    def work_with_dog(self, dog):
        dog.work()
p=Person()
dog1=armyDog()
dog2=drugDog()
p.work_with_dog(dog1)
p.work_with_dog(dog2)
# MRO
print(armyDog.__mro__)
print(drugDog.mro())


