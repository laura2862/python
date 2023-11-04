import re

import requests


def get_gdp():
    data=requests.get("http://127.0.0.1:8088/gdp.html")
    data=data.content.decode()
    country=re.findall('.*<a href=""><font>(.*)</font></a>',data)
    gdp=re.findall('￥(.*)亿元',data)
    return list(zip(country, gdp))



if __name__ == '__main__':
    print(get_gdp()) 
