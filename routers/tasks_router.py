"""The router file for tasks"""
from fastapi import APIRouter, HTTPException, status
from models.tasks_model import Task
from typing import List


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks_router():
    """Get all tasks"""
    try:
        tasks = await Task.find_all().to_list()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

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
