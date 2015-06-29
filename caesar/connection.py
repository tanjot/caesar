#!/usr/bin/python3

import smtplib
import socket

from .mail import get_password_from_file
from colorama import init
from colorama import Fore

init()

class Connection:

    def create_conn(self, host, port):
        try:
            self.server = smtplib.SMTP(host, port)
            self.server.set_debuglevel(True)
            self.server.ehlo()
            self.server.starttls()
        except ConnectionRefusedError:
            print(Fore.RED + 'connection refused')
        except socket.gaierror:
            print(Fore.RED + 'problem connecting with host, check hostname or port')
        except smtplib.SMTPAuthenticationError:
            print(Fore.RED + 'invalide username or password')



    def send_mail(self, msg):

        try:
            password = get_password_from_file(msg['from'])
            self.server.login(msg['from'], password)
            self.server.sendmail(msg['from'], msg['to'], msg.as_string())
            self.server.close()
        except smtplib.SMTPAuthenticationError:
            print(Fore.RED+'Username/Password could not be authenticated')
        except smtplib.SMTPServerDisconnected:
            print(Fore.RED + 'Connection got disconnected')
