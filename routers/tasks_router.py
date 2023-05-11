"""The router file for tasks"""
from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/tasks")
async def get_all_tasks():
    """Get all tasks"""
    return {"tasks": []}


@tasks_router.get("/tasks/{task_id}")
async def get_single_router(task_id: int):
    """Get a single task"""
    return {"task": task_id}


@tasks_router.post("/tasks")
async def create_router():
    """Create a task"""
    return {"task": "created"}


@tasks_router.put("/tasks/{task_id}")
async def update_router(task_id: int):
    return {"task": task_id}


@tasks_router.delete("/tasks/{task_id}")
async def delete_router(task_id: int):
    return {"task": task_id}
