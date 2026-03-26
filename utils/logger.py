import os
import logging
from logging.handlers import RotatingFileHandler

def get_logger(name: str):
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO) 
    if not logger.handlers:
        handler = RotatingFileHandler(
            "logs/whatsapp.log",
            maxBytes=5_000_000,
            backupCount=3
        )
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())

    return logger