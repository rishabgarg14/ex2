import logging
import inspect
import os


def customLogger(loglevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(loglevel)

    currentDirectory = os.path.dirname(__file__)
    logPath = "../automation.log"
    logFile = os.path.join(currentDirectory, logPath)
    fileHandler = logging.FileHandler(logFile, mode='a')
    # fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%y %I:%M:%S')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger
