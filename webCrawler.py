import re
import requests
new_list = []
# opt+cmd+m: extract code as a function
def get_pic_url():
    data = requests.get("http://127.0.0.1:8088/index.html")
    data = data.content.decode("utf-8")
    datalist = data.split('\n')
    for i in datalist:
        url = re.match('.*src="(.*?)"', i)
        if url:
            # print(url.group(1))
            global new_list
            new_list.append(url.group(1))
    return new_list

def save_pic(new_list):
    for index,url in enumerate(new_list):
        print(f'index is {index},url is {url}')
        pic=requests.get(f'http://127.0.0.1:8088{url[2:]}')
        with open(f'./images/download_images/{index}.jpg','wb') as f:
            f.write(pic.content)




if __name__ == '__main__':
    pics=get_pic_url()
    save_pic(pics)




