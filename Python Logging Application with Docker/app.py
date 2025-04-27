# app.py
import os
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/data/app.log'),
        logging.StreamHandler()
    ]
)

# Ensure log directory exists
os.makedirs("/data", exist_ok=True)

logger = logging.getLogger(__name__)

while True:
    logger.info("Application is running")
    time.sleep(5)