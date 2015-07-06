#!/usr/bin/python3

from os import path

class Credentials:

    def __init__(self, logger):
        self.logger = logger
        self.cred_filename = path.join(path.expanduser('~'), 'caesar_user.conf')
        self.server_conf_filename = path.join(path.expanduser('~'), 'caesar_server.conf')

    def save_email_password(self, email, pwd):
        with open(self.cred_filename, 'a') as fhan:
            fhan.write(email+'\n')
            fhan.write(pwd+'\n')

    def get_password(self, email_recv):
        pwd=None

        try:
            fhan = open(self.cred_filename, 'r')
            email = fhan.readline().strip()
            while email:
                if email == email_recv:
                    pwd = fhan.readline().strip()
                    break
                fhan.readline()
                email=fhan.readline().strip()
        except StopIteration:
            fhan.close()
        except FileNotFoundError:
            print('Configuration file does not exist')

        return pwd


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
            print('Configuration file does not exist')

        #Following case will not create connection, gives SMTPServerDisconnected
        #exception
        if host is None or port is None:
            print('Problem finding the specified settings. Either the settings'
            'stored are incorrect or server configuration file does not exist')

        return host, port
