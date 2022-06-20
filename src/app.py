from fastapi import FastAPI
import logging
from src.api import router
from utils import get_project_root

app = FastAPI()  # Create application instance
app.include_router(router)  # Register endpoints


@app.on_event("startup")
async def startup_event():
    project_root = await get_project_root()
    logger = logging.getLogger("uvicorn.access")
    handler = logging.FileHandler(project_root.joinpath("server_logs.log"))
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
