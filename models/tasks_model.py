"""The tasks model file"""
from datetime import datetime

from beanie import Document
from pydantic import Field


class Task(Document):
    """The task model

    Args:
        Document (Beanie): The base document class
    """
    task_content: str = Field(max_length=400)
    is_complete: bool
    date_created: datetime

    class Settings:
        name = "TasksDB"

    class Config:
        schema_extra = {
            "task_content": "This is a task",
            "is_complete": False,
            "date_created": "2021-01-01"
        }
