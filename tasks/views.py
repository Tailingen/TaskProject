from fastapi import APIRouter

from tasks.schemas import TaskAddSchema

router = APIRouter(prefix='/tasks', tags=['tasks', ])

db_immitation = [
    {'id': 1, 'text': 'Полить цветы', 'status': False},
    {'id': 2, 'text': 'Погулять с собакой', 'status': False}
]

@router.get('/{task_id}/')
async def task(task_id: int):
    if len(db_immitation) >= task_id > 0:
        return db_immitation[task_id-1]['text']
    else:
        return 'Запись не найдена'

@router.get('/')
async def tasks():
    return db_immitation

@router.post('/create/')
async def task_create(schema: TaskAddSchema):
    db_immitation.append({'id': len(db_immitation)+1, 'text': schema.text, 'status': schema.status})
    return db_immitation[-1]

@router.put('/{task_id}/update/')
async def task_update(task_id: int, schema: TaskAddSchema):
    if len(db_immitation) >= task_id > 0:
        db_immitation[task_id-1] = {'id': task_id, 'text': schema.text, 'status': schema.status}
        return db_immitation[task_id-1]
    else:
        return 'Запись не найдена'

@router.delete('/{task_id}/delete/')
async def task_delete(task_id: int):
    task_deleted = db_immitation.pop(task_id-1)
    return task_deleted