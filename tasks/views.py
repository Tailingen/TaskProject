from fastapi import APIRouter
from sqlalchemy import insert, update, delete, select

from models import engine, TaskModel
from tasks.schemas import TaskAddSchema

router = APIRouter(prefix='/tasks', tags=['tasks', ])

@router.get('/{task_id}/')
async def task(task_id: int):
    async with engine.connect() as conn:
        query = select(TaskModel).filter(TaskModel.id == task_id)
        res = await conn.execute(query)
    return list(res.first())

@router.get('/')
async def tasks():
    async with engine.connect() as conn:
        query = select(TaskModel)
        res = await conn.execute(query)
    return [list(i) for i in res.all()]

@router.post('/create/')
async def task_create(schema: TaskAddSchema):
    async with engine.connect() as conn:
        query = insert(TaskModel).values(text=schema.text, status=schema.status)
        await conn.execute(query)
        await conn.commit()
    return schema

@router.put('/{task_id}/update/')
async def task_update(task_id: int, schema: TaskAddSchema):
    async with engine.connect() as conn:
        query = update(TaskModel).filter(TaskModel.id == task_id).values(text=schema.text, status=schema.status)
        await conn.execute(query)
        await conn.commit()
    return schema

@router.delete('/{task_id}/delete/')
async def task_delete(task_id: int):
    async with engine.connect() as conn:
        query = delete(TaskModel).filter(TaskModel.id == task_id)
        await conn.execute(query)
        await conn.commit()
    return {'status': 'Запись удалена'}