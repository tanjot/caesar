#!/usr/bin/python3

import smtplib
import getpass
from colorama import Fore
from colorama import init
import socket

init()

def read_data_from_file():

    filename = input('Enter file to read data: ')

    fhan = open( filename, 'r')

    return fhan.read()


def main():

    try:

        mail = smtplib.SMTP(host='smtp.gmail.com', port=587)

        mail.set_debuglevel(True)

        mail.ehlo()

        mail.starttls()

        email = input('Enter login details\nEmail: ')
        password = getpass.getpass('Enter password: ')
        mail.login(email, password)

        content = read_data_from_file()

        receiver = input('Enter recipients address: ')

        mail.sendmail(email, receiver, content)

        mail.close()
    except ConnectionRefusedError:
        print(Fore.RED+'Connection refused')
    except socket.gaierror:
        print(Fore.RED+'Problem connecting with host, check hostname or port')
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+'Invalide username or password')


if __name__ == '__main__':
    main()














