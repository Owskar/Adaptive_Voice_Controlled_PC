# utils/logger.py
import logging
import os


def setup_logger():
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("logs/assistant.log"), logging.StreamHandler()],
    )

    return logging.getLogger("assistant")


logger = setup_logger()
logger.info("Application started")
