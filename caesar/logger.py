#!/usr/bin/python3

import logging
import sys

VERBOSITY_LEVELS = {
                    'debug' : logging.DEBUG,
                    'error' : logging.ERROR,
                    'info'  : logging.INFO
                    }

class Logger:
    def __init__(self):
        verbosity = VERBOSITY_LEVELS['info']

        log_format = logging.Formatter('%(message)s')

        stream_handle = logging.StreamHandler(sys.stdout)
        stream_handle.setFormatter(log_format)

        self.log_handle = logging.getLogger(__name__)
        self.log_handle.setLevel(verbosity)

        self.log_handle.addHandler(stream_handle)

    def print_log(self, msg, verbosity=VERBOSITY_LEVELS['info']):
        self.log_handle.log(verbosity, msg)
