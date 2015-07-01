#!/usr/bin/python3

import logging
import sys

from colorama import init
from colorama import Fore

init(autoreset=True)

VERBOSITY_LEVELS = {
                    'debug' : logging.CRITICAL,
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
        if verbosity == VERBOSITY_LEVELS['debug']:
            self.log_handle.log(verbosity, Fore.CYAN+msg)

        elif verbosity == VERBOSITY_LEVELS['error']:
            self.log_handle.log(verbosity, Fore.RED+msg)

        else:
            self.log_handle.log(verbosity, Fore.MAGENTA+msg)
