"""Created the entrypoint for the application"""
import uvicorn
from fastapi import FastAPI
from routers.tasks_router import tasks_router


app = FastAPI()


@app.get("/", name="Home", description="The root endpoint for the application", tags=["Home"])
async def root():
    """The root endpoint for the application"""
    return {"message": "Hello World"}


app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0000000", port=8000, reload=True)
