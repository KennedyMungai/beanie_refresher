"""Will contain the db connection logic"""
import os

import motor
from beanie import init_beanie
from dotenv import find_dotenv, load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from models.tasks_model import Task

load_dotenv(find_dotenv())

MONGODB_URL = os.environ.get("MONGODB_URL")


async def init_db():
    """Handles the database connection logic"""
    db_client = AsyncIOMotorClient(MONGODB_URL).tasks
    await init_beanie(database=db_client, document_models=[Task])
