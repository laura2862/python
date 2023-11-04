import re
import threading
# task 1
import requests


def task_1():
    pic=get_pic()
    save_pic(pic)


def get_pic():
    data=requests.get("http://127.0.0.1:8088")
    data=data.content.decode().split()
    pic=[]
    for i in data:
        url=re.match('.*src="(.*?)"',i)
        if url:
            pic.append(url.group(1))
    return pic
def save_pic(pic):
    for index, i in enumerate(pic):
        url=requests.get(f"http://127.0.0.1:8088{i[2:]}")
        with open(f'./images/download_images/{index}.jpg','wb') as f:
            f.write(url.content)
# task 2
def task_2():
    gdp = get_gdp()
    save_gdp(gdp)
def get_gdp():
    data=requests.get("http://127.0.0.1:8088/gdp.html")
    data=data.content.decode()
    # get country
    country=re.findall('.*<a href=""><font>(.*)</font></a>',data)
    # get gdp
    gdp = re.findall('.*￥(.*)亿元', data)
    gdplist=list(zip(country,gdp))
    return gdplist
def save_gdp(list):
    with open('./downloads/mutiThreadGdpCrawler.txt','wb',encoding='utf-8') as f:
        f.write(str(list))
    print(f)
# main
if __name__ == '__main__':
    t1=threading.Thread(target=task_1)
    t2=threading.Thread(target=task_2)
    t1.start()
    t2.start()

