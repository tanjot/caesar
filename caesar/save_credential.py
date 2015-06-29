#!/usr/bin/python3

from os import path

cred_filename = path.join(path.expanduser('~'), 'caesar_user.conf')
server_conf_filename = path.join(path.expanduser('~'), 'caesar_server.conf')

def save_email_password(email, pwd):
    with open(cred_filename, 'a') as fhan:
        fhan.write(email+'\n')
        fhan.write(pwd+'\n')

def get_password(email_recv):
    pwd=None

    try:
        fhan = open(cred_filename, 'r')
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


def save_server_conf(name, host, port):
    with open(server_conf_filename, 'a')as fhan:
        fhan.write(name+'\n')
        fhan.write(host+':'+port+'\n')


