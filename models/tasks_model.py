"""The tasks model file"""
from beanie import Document
from datetime import datetime
from pydantic import Field


class Task(Document):
    task_content: str
    is_complete: bool
    date_created: datetime
