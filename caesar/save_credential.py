#!/usr/bin/python3

from email import encoders
filename='credentials.txt'

def save_email_password(email, pwd):
    with open(filename, 'a') as fhan:
        fhan.write(email+'\n')
        fhan.write(pwd+'\n')

def get_password(email_recv):
    pwd=None
#    with open(filename, 'r+') as fhan:
#        email = fhan.readline().strip()
#        if email == email_recv:
#            pwd = fhan.readline()
#            return pwd
#        fhan.readline()

    fhan = open(filename, 'r')

    try:
        email = fhan.readline().strip()
        while email:
            if email == email_recv:
                pwd = fhan.readline().strip()
                break
            fhan.readline()
            email=fhan.readline().strip()
    except StopIteration:
        fhan.close()

    return pwd




