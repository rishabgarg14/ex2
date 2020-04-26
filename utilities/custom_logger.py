import logging
import inspect

def customLogger(loglevel=logging.DEBUG):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\automation.log", mode='a')
    # fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%y %I:%M:%S')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger