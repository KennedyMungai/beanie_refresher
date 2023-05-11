"""The router file for tasks"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import ConnectionFailure
from schemas.tasks_schemas import TaskUpdate

from models.tasks_model import Task

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks_router() -> List[Task]:
    """Get all tasks"""
    try:
        tasks = await Task.find().to_list()
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return tasks


@tasks_router.get("/{task_id}")
async def get_single_task_router(task_id: PydanticObjectId) -> Task:
    """Get a single task"""
    try:
        single_task = await Task.get(task_id)
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    if not single_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return single_task


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
async def update_task_router(_task_id: PydanticObjectId, _task: Task) -> Task:
    """The endpoint for updating tasks

    Args:
        _task_id (PydanticObjectId): The id of an individual task
        _task (Task): The new task data

    Raises:
        HTTPException: Raised when a good connection to the database could not be established
        HTTPException: Raised when the task cannot be found

    Returns:
        Task: The newly updated task
    """
    try:
        _single_task = await Task.get(_task_id)
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    if not _single_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    _single_task.task_content = _task.task_content
    _single_task.task_completed = _task.task_completed

    await _single_task.save()

    return _single_task


@tasks_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_router(task_id: PydanticObjectId):
    """The delete endpoint

    Args:
        task_id (PydanticObjectId): The id of the task

    Raises:
        HTTPException: The internal server error HTTPException
        HTTPException: _description_
    """
    try:
        _task_to_delete = await Task.get(task_id)
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    if _task_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    await _task_to_delete.delete()
    await _task_to_delete.save()

    return None
