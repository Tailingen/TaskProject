import asyncio

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_async_engine(url='sqlite+aiosqlite:///test.db', echo=True)

class Base(DeclarativeBase):
    pass

#Таблицы

class TaskModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    status: Mapped[bool]

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with engine.connect() as conn:
        query = select(TaskModel).filter(TaskModel.id == 1)
        res = await conn.execute(query)
        print(res.first())
        # print(query.compile(compile_kwargs={'literal_binds': True}))
    # async with engine.connect() as conn:
    #     query = insert(TaskModel).values(id=4, text='Купить шляпу', status=False)
    #     await conn.execute(query)
    #     await conn.commit()
    # async with engine.connect() as conn:
    #     query = update(TaskModel).filter(TaskModel.id == 1).values(text='Постричь кактус!')
    #     await conn.execute(query)
    #     await conn.commit()


# asyncio.run(create_db())