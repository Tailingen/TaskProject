from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

db_immitation = [
    {'id': 1, 'text': 'Полить цветы', 'status': False},
    {'id': 2, 'text': 'Погулять с собакой', 'status': False}
]

class TaskAddSchema(BaseModel):
    text: str = Field(min_length=2, max_length=255)
    status: bool = False

@app.get('/home/')
async def home():
    return 'Home'

@app.get('/about/')
async def about():
    return 'Страница о сайте'

@app.get('/tasks/{task_id}/')
async def task(task_id: int):
    if len(db_immitation) >= task_id > 0:
        return db_immitation[task_id-1]['text']
    else:
        return 'Запись не найдена'

@app.get('/tasks/')
async def tasks():
    return db_immitation

@app.post('/tasks/create/')
async def task_create(schema: TaskAddSchema):
    db_immitation.append({'id': len(db_immitation)+1, 'text': schema.text, 'status': schema.status})
    return db_immitation[-1]

@app.put('/tasks/{task_id}/update/')
async def task_update(task_id: int, schema: TaskAddSchema):
    if len(db_immitation) >= task_id > 0:
        db_immitation[task_id-1] = {'id': task_id, 'text': schema.text, 'status': schema.status}
        return db_immitation[task_id-1]
    else:
        return 'Запись не найдена'

@app.delete('/tasks/{task_id}/delete/')
async def task_delete(task_id: int):
    task_deleted = db_immitation.pop(task_id-1)
    return task_deleted