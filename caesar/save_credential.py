#!/usr/bin/python3

import base64
from os import path
from .logger import VERBOSITY_LEVELS

class Credentials:

    def __init__(self, logger):
        self.logger = logger
        self.cred_filename = path.join(path.expanduser('~'), 'caesar_user.conf')
        self.server_conf_filename = path.join(path.expanduser('~'), 'caesar_server.conf')

    def save_email_password(self, email, pwd):
        with open(self.cred_filename, 'ab') as fhan:
            fhan.write(bytes(email+'\n', 'UTF-8'))
            fhan.write(base64.b64encode(pwd.encode('UTF-8')))#bytes(pwd+'\n', 'UTF-8'))
            fhan.write(bytes('\n', 'UTF-8'))

    def check_email_exists(self, email_recv):

        try:
            fhan = open(self.cred_filename, 'r')
            email = fhan.readline().strip()
            while email:
                if email == email_recv:
                    return True

                fhan.readline()
                email=fhan.readline().strip()
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')
            return False

        return False


    def get_password(self, email_recv):
        pwd=None

        try:
            fhan = open(self.cred_filename, 'r')
            email = fhan.readline().strip()
            while email:
                if email == email_recv:
                    pwd = base64.b64decode(fhan.readline().strip()).decode('UTF-8')
                    break
                fhan.readline()
                email=fhan.readline().strip()
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')

        return pwd

    def check_server_exists(self, host_name_recv):

        try:
            fhan = open(self.server_conf_filename, 'r')
            host_name = fhan.readline().strip()
            while host_name:
                if host_name == host_name_recv:
                    return True
                fhan.readline()
                host_name = fhan.readline().strip()
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'Configuration file does not exist')
            return False

        return False


    def save_server_conf(self, name, host, port):
        with open(self.server_conf_filename, 'a')as fhan:
            fhan.write(name+'\n')
            fhan.write(host+':'+port+'\n')

    def get_server_conf(self, host_name_recv):
        host = None
        port = None

        try:
            fhan = open(self.server_conf_filename, 'r')
            host_name = fhan.readline().strip()
            while host_name:
                if host_name == host_name_recv:
                    line = fhan.readline().strip().split(':')
                    host=line[0]
                    port=line[1]
                    break
                fhan.readline()
                host_name = fhan.readline().strip()
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
