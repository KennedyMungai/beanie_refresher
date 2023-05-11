"""Will contain the db connection logic"""
import motor
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.tasks_model import Task


async def init_db():
    """Handles the database connection logic"""
    db_client = AsyncIOMotorClient("mongodb://localhost:27017")
    init_beanie(database="Tasks", document_models=[Task])
