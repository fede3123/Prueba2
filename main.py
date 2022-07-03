from fastapi import FastAPI

app = FastAPI()


def createDb(quantity):
    result = [(x, 'q') for x in range(quantity)]
    return result


db = createDb(1000000)


@app.get("/")
async def root():
    return 'Hola'


@app.get('/request/${page_num}&${page_size}')
async def request(page_num: int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size
    return db[start:end]


@app.get('/find/${id}')
async def find(id: int):
    for key, value in db:
        if key == id:
            return db[key]
