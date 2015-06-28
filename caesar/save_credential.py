#!/usr/bin/python3

from os import path

filename = path.join(path.expanduser('~'), 'caesar.conf')

def save_email_password(email, pwd):
    with open(filename, 'a') as fhan:
        fhan.write(email+'\n')
        fhan.write(pwd+'\n')

def get_password(email_recv):
    pwd=None


    try:
        fhan = open(filename, 'r')
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




