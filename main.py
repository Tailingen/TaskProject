from fastapi import FastAPI

from tasks.views import router

app = FastAPI()
app.include_router(router)

@app.get('/home/')
async def home():
    return 'Home'

@app.get('/about/')
async def about():
    return 'Страница о сайте'

