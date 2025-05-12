from fastapi import FastAPI
from utils.logger import setup_logger

logger = setup_logger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to TorchFlow Backend!"}