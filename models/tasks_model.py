"""The tasks model file"""
from datetime import datetime

from beanie import Document
from pydantic import Field


class Task(Document):
    """The task model

    Args:
        Document (Beanie): The base document class
    """
    task_content: str
    is_complete: bool
    date_created: datetime
