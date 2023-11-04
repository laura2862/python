import re
import requests
from pyecharts.charts import Pie
from pyecharts import options as opts
def get_pie(data):
    pie=Pie(init_opts=opts.InitOpts(width='1200px',height='800px'))
    pie.add(
        'laura\'s GDP',
        data[:10],
        label_opts=opts.LabelOpts(formatter='{a}:{b}%')
    )
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title='The world GDP',subtitle='@Laura')
    )
    pie.render('./html/myRender.html')
def get_data():
    data=requests.get("http://127.0.0.1:8088/gdp.html")
    data=data.content.decode()
    country=re.findall('.*<a href=".*?"><font>(.*?)</font></a>',data)
    gdp=re.findall('.*￥(.*)亿元',data)
    return list(zip(country,gdp))
if __name__ == '__main__':
    data=get_data()
    get_pie(data)