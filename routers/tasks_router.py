"""The router file for tasks"""
from fastapi import APIRouter
from models.tasks_model import Task
from typing import List


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks_router() -> List[Task]:
    """Get all tasks"""
    tasks = await Task.find_all().tolist()
    return tasks


@tasks_router.get("/{task_id}")
async def get_single_task_router(task_id: int):
    return {"task": task_id}


@tasks_router.post("/")
async def create_task_router():
    return {"task": "created"}


@tasks_router.put("/{task_id}")
async def update_task_router(task_id: int):
    return {"task": task_id}


@tasks_router.delete("/{task_id}")
async def delete_task_router(task_id: int):
    return {"task": task_id}
