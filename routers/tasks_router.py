"""The router file for tasks"""
from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])
