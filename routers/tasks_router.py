"""The router file for tasks"""
from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/")
async def get_all_tasks():
    """Get all tasks"""
    return {"tasks": []}
