#!/usr/bin/python3

import smtplib
import socket

from .mail import get_password_from_file
from colorama import init

init()

class Connection:

    def create_conn(self):
        try:
            self.server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            self.server.set_debuglevel(True)
            self.server.ehlo()
            self.server.starttls()
        except ConnectionRefusedError:
            print(fore.red + 'connection refused')
        except socket.gaierror:
            print(fore.red + 'problem connecting with host, check hostname or port')
        except smtplib.SMTPAuthenticationError:
            print(fore.red + 'invalide username or password')



    def send_mail(self, msg):

        password = get_password_from_file(msg['from'])
        self.server.login(msg['from'], password)
        self.server.sendmail(msg['from'], msg['to'], msg.as_string())
        self.server.close()
