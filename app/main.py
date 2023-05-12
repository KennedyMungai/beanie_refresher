"""Created the entrypoint for the application"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import init_db
from routers.tasks_router import tasks_router

app = FastAPI(title="Tasks CRUD Application")

origins = [
    'http://localhost:3000',
    'https://localhost:3000',
    'http://localhost:3000/tasks',
    'https://localhost:3000/tasks',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initializes the database"""
    print("Initializing database...")
    await init_db()


@app.get("/", name="Home", description="The root endpoint for the application", tags=["Home"])
async def root():
    """The root endpoint for the application"""
    return {"message": "Hello World"}


app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0000000", port=8000, reload=True)
