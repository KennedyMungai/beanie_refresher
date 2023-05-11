"""The router file for tasks"""
from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks_router():
    return {"tasks": []}


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