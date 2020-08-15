#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import configparser


try:
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    default_log_file = config.get("LOGS", 'log_file')
except Exception as e:
    raise Exception("Config file reading error: " + str(e))


class LoggingModule():
    def __init__(self, name=None, log_file_loc=None, debug_level=None):
        if name == None:
            raise Exception("Expected parameter: name, loffileloc and optional parameter debug_level ")
        if log_file_loc == None:
            self.log_file_loc = default_log_file
        else:
            self.log_file_loc = log_file_loc
        if debug_level == None:
            print("Using default debug_level 2")
            debug_level = 2
        self.name = name
        self.debug_level = debug_level

    def getlogger(self):
        self.logger = logging.getLogger(self.name)
        if self.debug_level == 0:
            self.logger.setLevel(logging.DEBUG)
        if self.debug_level == 1:
            self.logger.setLevel(logging.INFO)
        if self.debug_level == 2:
            self.logger.setLevel(logging.ERROR)
        handler = logging.handlers.RotatingFileHandler(self.log_file_loc,
                                                       maxBytes=20000000,
                                                       backupCount=100)
        formatter = logging.Formatter('[%(asctime)s] '
                                      'p%(process)s '
                                      '{%(name)s:%(lineno)d} '
                                      '%(levelname)s - '
                                      '%(message)s',
                                      '%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        logger_obj = self.logger
        return logger_obj
