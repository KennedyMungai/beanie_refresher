"""Created the entrypoint for the application"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/", name="Home", description="The root endpoint for the application", tags=["Home"])
async def root():
    """The root endpoint for the application"""
    return {"message": "Hello World"}
