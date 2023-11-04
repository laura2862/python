import logging
import uvicorn
from fastapi import FastAPI,Response
app=FastAPI()
logging.basicConfig(
    level=logging.DEBUG,
    format=f'%(asctime)s visited %(filename)s: %(message)s-----%(lineno)d-----%(levelname)s',
    filename='webLog.txt',
    filemode='w'
)

@app.get('/')
def show():
    with open('html/index.html','rb') as f:
       data= f.read()
       logging.info(f'visited index.html.....')
       return Response(content=data)

@app.get('/{path}')
def show(path:str):
    with open(f'html/{path}','rb') as f:
        data=f.read()
        logging.info(f'visited {path}.....')
        return Response(content=data)
@app.get('/images/{path}')
def show(path:str):
    with open(f'images/{path}','rb') as f:
        data = f.read()
        logging.info(f'visited {path} ....')
        return Response(content=data)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8090)
