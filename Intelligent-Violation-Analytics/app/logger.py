import logging
import os
from datetime import datetime

LOG_FILE = "logs/app.log"

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("debug_monitor")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s'
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()


def log_info(message, data=None):
    logger.info(f"{message} | {data}")


def log_error(message, error=None):
    logger.error(f"{message} | {error}")


def log_debug(message):
    logger.debug(message)


def log_performance(event_name, start_time):
    import time
    duration = round((time.time() - start_time) * 1000, 2)
    logger.info(f"{event_name} took {duration} ms")
