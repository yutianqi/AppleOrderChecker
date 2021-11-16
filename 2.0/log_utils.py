import logging
from logging.handlers import RotatingFileHandler


class LogUtils(object):

    logger = logging.getLogger(__name__)

    LOG_FILE_PATH = 'run.log'

    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler(LOG_FILE_PATH)
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(fileHandler)

    streamHandler = logging.StreamHandler() 
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(streamHandler)

    @classmethod
    def info(cls, logMsg):
        cls.logger.info(logMsg)

# LogUtils.info('This is a info log from main')
