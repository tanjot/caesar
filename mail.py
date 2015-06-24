#!/usr/bin/python3

import smtplib
import getpass
from colorama import Fore
from colorama import init
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import socket
import os

init()

def read_data_from_file():
    filename = input('Enter file to read data: ')
    fhan = open(filename, 'r')
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

def get_password():
    return getpass.getpass('Enter password: ')

def prepare_msg():
    msg = MIMEMultipart()
    #msg = MIMEText(read_data_from_file())
    msg.attach(attach_file())
    msg['To'] = input('Enter recipients address: ')
    msg['From'] = get_email()
    msg['Subject'] = 'Mailing using python'
    return msg


def main():
    try:
        mail = smtplib.SMTP(host='smtp.gmail.com', port=587)
        mail.set_debuglevel(True)
        mail.ehlo()
        mail.starttls()
        msg = prepare_msg()
        password = get_password()
        mail.login(msg['From'], password)
        mail.sendmail(msg['From'], msg['To'], msg.as_string())
        mail.close()
    except ConnectionRefusedError:
        print(Fore.RED + 'Connection refused')
    except socket.gaierror:
        print(Fore.RED + 'Problem connecting with host, check hostname or port')
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED + 'Invalide username or password')


if __name__ == '__main__':
    main()
