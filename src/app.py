from fastapi import FastAPI

from src.api import router

app = FastAPI()  # Create application instance
app.include_router(router)  # Register endpoints
