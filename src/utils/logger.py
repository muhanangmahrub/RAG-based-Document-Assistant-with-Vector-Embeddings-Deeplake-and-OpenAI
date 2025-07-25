import os
from loguru import logger
from src.config.settings import LOG_PATH, LOG_LEVEL

LOG_DIR = LOG_PATH
LOG_LEVEL = LOG_LEVEL

LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)
logger.remove()  # Remove default logger
logger.add(LOG_FILE, rotation="1 MB", level=LOG_LEVEL, backtrace=True, diagnose=True)
