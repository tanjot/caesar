#!/usr/bin/python3

from os import path
from .logger import VERBOSITY_LEVELS
from .utils import read_dict_from_file
from .utils import append_key_value_to_file
from .utils import write_dict_to_file
from .utils import encode_data
from .utils import decode_data

class Credentials:

    def __init__(self, logger):
        self.logger = logger
        self.cred_filename = path.join(path.expanduser('~'), 'caesar_user.conf')
        self.server_conf_filename = path.join(path.expanduser('~'), 'caesar_server.conf')

        self.dict_server = {}
        self.dict_user = {}

        self.dict_server = read_dict_from_file(self.server_conf_filename)

        self.dict_user = read_dict_from_file(self.cred_filename)

    def save_email_password(self, email, pwd):
        append_key_value_to_file(self.cred_filename, email, encode_data(pwd))

    def replace_password(self, email, pwd):
        self.dict_user[email] = encode_data(pwd);
        write_dict_to_file(self.server_conf_filename, self.dict_user)

    def check_email_exists(self, email_recv):

        try:
            if self.dict_user is not None and email_recv in self.dict_user:
                return True
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')
            return False

        return False


    def get_password(self, email_recv):
        pwd=None

        try:
            if self.dict_server is not None and email_recv in self.dict_user:
                pwd = decode_data(self.dict_user[email_recv])
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')

        return pwd

    def check_server_exists(self, host_name_recv):

        try:
            if self.dict_server is not None and host_name_recv in self.dict_server:
                return True
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')
            return False

        return False


    def save_server_conf(self, name, host, port):
        append_key_value_to_file(self.server_conf_filename, name, host+','+port)

    def get_server_conf(self, host_name_recv):
        host = None
        port = None

        try:
            host, port = (self.dict_server.get(host_name_recv)).split(',')
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration '
                    'file does not exist')
            self.logger.print_log(VERBOSITY_LEVELS['info'
            ], 'Add mailing client\'s IP and port using -ss argument')

        #Following case will not create connection, gives SMTPServerDisconnected
        #exception
        if host is None or port is None:
            self.logger.print_log(VERBOSITY_LEVELS['info'], 'Problem finding the specified settings. Either the settings'
            ' stored are incorrect or server configuration does not exist')

        return host, port
