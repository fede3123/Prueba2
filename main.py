from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


def createDb(quantity):
    arr = [(uuid.uuid4(), x) for x in range(quantity)]
    result = {}
    for key, value in arr:
        result[key] = value

    return result


@app.get("/")
async def root():
    return templates.TemplateResponse('base.html', {})


@app.get('/request')
async def request():
    db = createDb(1000000)
    return templates.TemplateResponse('response.html', {'db': db})
