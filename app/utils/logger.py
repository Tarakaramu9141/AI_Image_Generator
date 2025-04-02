from loguru import logger
import sys

def setup_logger():
    logger.remove()
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )
    logger.add(
        "logs/app.log",
        rotation="500 MB",
        retention="7 days",
        level="DEBUG"
    )
    return logger