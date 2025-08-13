from sqlalchemy import select, insert, update, delete

from models import engine, TaskModel


async def read_task(task_id: int):
    async with engine.connect() as conn:
        query = select(TaskModel).filter(TaskModel.id == task_id)
        res = await conn.execute(query)
    return res.first()

async def read_tasks():
    async with engine.connect() as conn:
        query = select(TaskModel)
        res = await conn.execute(query)
    return res

async def create_task(schema):
    async with engine.connect() as conn:
        query = insert(TaskModel).values(text=schema.text, status=schema.status)
        await conn.execute(query)
        await conn.commit()
    return schema

async def update_task(task_id: int, schema):
    async with engine.connect() as conn:
        query = update(TaskModel).filter(TaskModel.id == task_id).values(text=schema.text, status=schema.status)
        await conn.execute(query)
        await conn.commit()
    return schema

async def delete_task(task_id: int):
    async with engine.connect() as conn:
        query = delete(TaskModel).filter(TaskModel.id == task_id)
        await conn.execute(query)
        await conn.commit()
    return {'status': 'Запись удалена'}
