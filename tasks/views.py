from fastapi import APIRouter
from sqlalchemy import insert, update, delete, select

from models import engine, TaskModel
from tasks.crud import read_task, read_tasks, create_task, update_task, delete_task
from tasks.schemas import TaskAddSchema

router = APIRouter(prefix='/tasks', tags=['tasks', ])

@router.get('/{task_id}/')
async def task(task_id: int):
    res = await read_task(task_id)
    return res

@router.get('/')
async def tasks():
    res = await read_tasks()
    return res

@router.post('/create/')
async def task_create(schema: TaskAddSchema):
    res = await create_task(schema)
    return res

@router.put('/{task_id}/update/')
async def task_update(task_id: int, schema: TaskAddSchema):
    res = await update_task(task_id, schema)
    return res

@router.delete('/{task_id}/delete/')
async def task_delete(task_id: int):
    res = await delete_task(task_id)
    return res