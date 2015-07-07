#!/usr/bin/python3

import logging
import sys

from colorama import init
from colorama import Fore

init()

#Order of verbosity TRACE>ERROR>INFO
TRACE=10
logging.addLevelName(TRACE, 'TRACE')

ERROR=30
logging.addLevelName(ERROR, 'ERROR')

INFO=50
logging.addLevelName(INFO, 'INFO')



VERBOSITY_LEVELS = {
                    'trace' : TRACE,    #3
                    'error' : ERROR,    #2
                    'info'  : INFO      #1
                    }

class Logger:
    def __init__(self, verbosity):

        self.logging_level = self.get_verbosity_level(verbosity)

        log_format = logging.Formatter('%(message)s')

        stream_handle = logging.StreamHandler(sys.stdout)
        stream_handle.setFormatter(log_format)

        self.log_handle = logging.getLogger(__name__)
        self.log_handle.setLevel(self.logging_level)

        self.log_handle.addHandler(stream_handle)

    def print_log(self, verbosity=VERBOSITY_LEVELS['info'], msg=None):
        if msg is not None:
            if verbosity == VERBOSITY_LEVELS['trace']:
                self.log_handle.log(verbosity, Fore.CYAN+msg)

            elif verbosity == VERBOSITY_LEVELS['error']:
                self.log_handle.log(verbosity, Fore.RED+msg)

            else:
                self.log_handle.log(verbosity, Fore.MAGENTA+msg)

        print(Fore.RESET)

    def get_verbosity_level(self, verbosity):
        ret_value = VERBOSITY_LEVELS['info']
        if (verbosity == 3):
            ret_value =  VERBOSITY_LEVELS['trace']
        elif (verbosity == 2):
            ret_value = VERBOSITY_LEVELS['error']

        return ret_value

