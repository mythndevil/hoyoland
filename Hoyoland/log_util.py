# -*- coding:utf-8 -*-

import logging
import logging.handlers

def getLogHandler(sLogerName, sLogFileName):
    fileMaxByte = 1024 * 1024 * 100 #100MB

    # Create logger instance
    logger = logging.getLogger(sLogerName)

    # Create formatter
    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    # Create log handler for printing to file
    fileHandler = logging.handlers.RotatingFileHandler(sLogFileName, maxBytes=fileMaxByte, backupCount=10)

    # Set handler with formatter
    fileHandler.setFormatter(formatter)

    # Add file handler to log handler
    logger.addHandler(fileHandler)

    # print log instance
    logger.setLevel(logging.INFO)

    return logger
