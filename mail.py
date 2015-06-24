#!/usr/bin/python3

import smtplib
import getpass
from colorama import Fore
from colorama import init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

init()

def read_data_from_file():

    filename = input('Enter file to read data: ')

    fhan = open( filename, 'r')

    content = fhan.read()

    fhan.close()

    return content
    


def prepare_msg():
    msg = MIMEMultipart()

    msg = MIMEText(read_data_from_file())

    msg['To'] = input('Enter recipients address: ')

    msg['From'] =  input('Enter login details\nEmail: ') 

    msg['Subject'] = 'Mailing using python'

    return msg
    

def main():

    try:

        mail = smtplib.SMTP(host='smtp.gmail.com', port=587)

        mail.set_debuglevel(True)

        mail.ehlo()

        mail.starttls()

        msg = prepare_msg()

        password = getpass.getpass('Enter password: ')
    
        mail.login(msg['From'], password)

        mail.sendmail(msg['From'], msg['To'], msg.as_string())

        mail.close()

    except ConnectionRefusedError:
        print(Fore.RED+'Connection refused')
    except socket.gaierror:
        print(Fore.RED+'Problem connecting with host, check hostname or port')
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED+'Invalide username or password')


if __name__ == '__main__':
    main()














