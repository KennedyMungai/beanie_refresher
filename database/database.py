"""Will contain the db connection logic"""
import motor
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.tasks_model import Task


async def init_db():
    """Handles the database connection logic"""
    db_client = AsyncIOMotorClient("mongodb://localhost:27017").tasks
    await init_beanie(database=db_client, document_models=[Task])
