#!/usr/bin/python3

import getpass

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from colorama import init
import os
from .save_credential import get_password

init()

def read_data_from_file():
    filename = input('Enter file to read data: ')

    fhan = open( filename, 'rb')

    content = fhan.read()
    fhan.close()
    return content, filename


def attach_file():
    base = MIMEBase('application', "octet-stream")
    content, filename = read_data_from_file()

    base.set_payload(content)
    encoders.encode_base64(base)
    base.add_header('Content-disposition', 'attachment', filename=filename)

    return base

def get_email():
    return input('Enter login details\nEmail: ')

def get_password_from_user():
    return getpass.getpass('Enter password: ')

def get_password_from_file(email):
    return get_password(email)

def prepare_msg():
    msg = MIMEMultipart()
    #msg = MIMEText(read_data_from_file())

    msg.attach(attach_file())
    msg['To'] = input('Enter recipients address: ')
    msg['Subject'] = input('Give a subject: ')
    msg['From'] = get_email()

    return msg

























