from fastapi import APIRouter, Form, status
from sqlalchemy import insert, update, delete, select
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from models import engine, TaskModel
from tasks.crud import read_task, read_tasks, create_task, update_task, delete_task
from tasks.schemas import TaskAddSchema

router = APIRouter(prefix='/tasks', tags=['tasks', ])

templates = Jinja2Templates(directory="templates")

@router.post('/create/')
async def task_create(request: Request, schema: TaskAddSchema = Form()):
    await create_task(schema)
    return RedirectResponse('/tasks/', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/create/')
async def task_create(request: Request):
    return templates.TemplateResponse(request, 'task_create.html')

@router.get('/{task_id}/')
async def task(request: Request, task_id: int):
    task_for_id = await read_task(task_id)
    return templates.TemplateResponse(request, 'task.html', {'task_for_id': task_for_id})

@router.get('/')
async def tasks(request: Request):
    task_list = await read_tasks()
    return templates.TemplateResponse(request, 'tasks.html', {'task_list': task_list})

@router.post('/{task_id}/update/')
async def task_update(task_id: int, schema: TaskAddSchema = Form()):
    await update_task(task_id, schema)
    return RedirectResponse(f'/tasks/{task_id}/', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/{task_id}/update/')
async def task_update(request: Request, task_id: int):
    task_for_id = await read_task(task_id)
    return templates.TemplateResponse(request, 'task_update.html', {'task_for_id': task_for_id})

@router.post('/{task_id}/delete/')
async def task_delete(task_id: int):
    await delete_task(task_id)
    return RedirectResponse('/tasks/', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/{task_id}/delete/')
async def task_delete(request: Request, task_id: int):
    task_for_id = await read_task(task_id)
    return templates.TemplateResponse(request, 'task_delete.html', {'task_for_id': task_for_id})