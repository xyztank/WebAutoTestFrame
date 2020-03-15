import os
import time
from loguru import logger


class MyLog:
    TIME = time.strftime('%Y-%m-%d')
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    LOG_PATH = BASE_DIR + '\\log\\'

    def mylogger(cls):
        logger.add(f'{cls.LOG_PATH}runtime_{cls.TIME}.log', encoding='utf-8', rotation='1 week', retention='10 days')
        return logger

    def close_logger(self):
        return logger.stop()
