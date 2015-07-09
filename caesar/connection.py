#!/usr/bin/python3

import smtplib
import socket

from .mail import Mail
from .logger import VERBOSITY_LEVELS
from colorama import init
from colorama import Fore

init()

class Connection:
    def __init__(self, logger ):
        self.logger = logger

    def create_conn(self, host, port):
        try:
            self.server = smtplib.SMTP(host, port)

            if self.logger.logging_level == VERBOSITY_LEVELS['trace']:
                self.server.set_debuglevel(True)
            self.server.ehlo()
            self.server.starttls()


        except ConnectionRefusedError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], Fore.RED + 'connection refused')
            return False
        except socket.gaierror:
            self.logger.print_log(VERBOSITY_LEVELS['error'],Fore.RED + 'problem connecting with host, check hostname or port')
            return False
        except smtplib.SMTPAuthenticationError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], Fore.RED + 'invalide username or password')
            return False
        except smtplib.SMTPServerDisconnected:
            self.logger.print_log(VERBOSITY_LEVELS['error'], Fore.RED + 'Server disconnected')
            return False

        return True

    def send_mail(self, msg):

        try:
            mail = Mail(self.logger)
            password = mail.get_password_from_file(msg['from'])
            self.server.login(msg['from'], password)
            self.server.sendmail(msg['from'], msg['to'], msg.as_string())
            self.server.close()
        except smtplib.SMTPAuthenticationError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], Fore.RED+'Username/Password could not be authenticated')
            return False
        except smtplib.SMTPServerDisconnected:
            self.logger.print_log(VERBOSITY_LEVELS['error'], Fore.RED + 'Connection got disconnected')
            return False

        return True
