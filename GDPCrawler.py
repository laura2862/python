import re 
import requests
def get_gdp():
    country = []
    gdp = []
    gdp_data = []
    data=requests.get('http://127.0.0.1:8088/gdp.html')
    data=data.content.decode('utf-8').split('\n')
    for i in data:
        country_result= re.match('.*<a href=".*?"><font>(.*?)</font></a>',i)
        if country_result:
            # print(country_result.group(1))
            country.append(country_result.group(1))
        gdp_result = re.match('.*￥(.*)亿元', i)
        if gdp_result:
            # print(gdp_result.group(1))
            gdp.append(gdp_result.group(1))
    gdp_data=list(zip(country,gdp))
    return gdp_data
def save_gdp(data):
    gdp_data = []
    for index, i in enumerate(data):
        gdp_data.append(i)
    print(gdp_data,type(gdp_data))
    with open('./downloads/gdp.txt','w',encoding='utf-8') as f:
        f.write(str(gdp_data))
    print(f)

if __name__ == '__main__':
    data=get_gdp()
    save_gdp(data)

