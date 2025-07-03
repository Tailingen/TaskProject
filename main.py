from fastapi import FastAPI

app = FastAPI()

db_immitation = [
    {'id': 1, 'text': 'Полить цветы'},
    {'id': 2, 'text': 'Погулять с собакой'}
]

@app.get('/home/')
def home():
    return 'Home'

@app.get('/about/')
def about():
    return 'Страница о сайте'

@app.get('/tasks/{task_id}/')
def task(task_id):
    if len(db_immitation) >= int(task_id) > 0:
        return db_immitation[int(task_id)-1]['text']
    else:
        return 'Запись не найдена'

@app.get('/tasks/')
def tasks():
    return db_immitation

@app.post('/tasks/create/')
def task_create(text):
    db_immitation.append({'id': len(db_immitation)+1, 'text': text})
    return db_immitation[-1]