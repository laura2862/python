from fastapi import Response, FastAPI
import uvicorn

app=FastAPI()
@app.get('/{path}')
def show(path:str):
    with open(f'html/{path}','rb') as f:
        data=f.read()
    return Response(content=data)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8080)





