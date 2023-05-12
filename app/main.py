"""Created the entrypoint for the application"""
import uvicorn
from fastapi import FastAPI
from routers.tasks_router import tasks_router
from database.database import init_db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Tasks CRUD Application")

app.add_middleware(
    CORSMiddleware,
    allowed_domains=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
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
