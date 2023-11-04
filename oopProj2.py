stars=[]
class Star():
    def __init__(self,name,movie):
        self.name=name
        self.movie=movie

    def playing(self):
        print(f'{self.name} played {self.movie} which is really good!!!')

def addStar():
    name=str(input('please input a star name:'))
    print(name)
    movie=str(input('please input his movie name:'))
    print(movie)
    p = Star(name,movie)
    stars.append(p)
def saveStar():
    f=open('star.txt','w',encoding='utf-8')
    for i in stars:
        f.write(f'{i.name}\n')
        f.write(f'{i.movie}\n')
    f.close()
def loadStar():
    f = open('star.txt', 'r', encoding='utf-8')
    content=Star()
    for i in range(len(f)):
        if not content:
            return
        elif i%2==0:
            content.name = f.readline()
        else:
            content.movie = f.readline()
        global stars
        stars.append(content)
        f.close()
def __str__(self):
    return f'i like {self.name}\'s {self.movie}'
if __name__ == '__main__':

    # for i in range(3):
        # addStar()
    # saveStar()
    loadStar()
    print(stars)
    print(type(stars))
    # for i in stars:
    #     # print(i)
    #     i.playing()






