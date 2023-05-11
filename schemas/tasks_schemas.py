"""The tasks schema file"""
from pydantic import BaseModel


class TaskUpdate(BaseModel):
    task_content: str
    is_complete: bool
