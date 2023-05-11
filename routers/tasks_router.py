"""The router file for tasks"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import ConnectionFailure

from models.tasks_model import Task

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks_router() -> List[Task]:
    """Get all tasks"""
    try:
        tasks = await Task.find_all().to_list()
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return tasks


@tasks_router.get("/{task_id}")
async def get_single_task_router(task_id: PydanticObjectId):
    return {"task": task_id}


@tasks_router.post("/", name="Create Task", description="Creates Tasks", status_code=status.HTTP_201_CREATED)
async def create_task_router(_task: Task) -> dict[str, str]:
    """The endpoint to create tasks

    Args:
        _task (Task): The task object

    Raises:
        HTTPException: Raises an internal server error if there is any error

    Returns:
        dict[str, str]: A message to show that the task has been created
    """
    try:
        await _task.create()
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {"message": "Task created successfully"}


@tasks_router.put("/{task_id}")
async def update_task_router(task_id: int):
    return {"task": task_id}


@tasks_router.delete("/{task_id}")
async def delete_task_router(task_id: int):
    return {"task": task_id}
