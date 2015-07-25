#!/usr/bin/python3

import getpass
import tempfile
import subprocess as sp
import os

from .logger import Logger
from .logger import VERBOSITY_LEVELS
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from .save_credential import Credentials
from .utils import input_for_python_2_3

input = input_for_python_2_3()

class Mail():

    def __init__(self, logger):
        self.logger = logger

    def read_data_from_file(self, filename=None):

        if filename is None:
            filename = input('Enter file to read data: ')

        fhan = open( filename, 'rb')

        content = fhan.read()
        fhan.close()
        return content, filename


    def attach_file(self, filename=None):
        base = MIMEBase('application', "octet-stream")
        content, filename = self.read_data_from_file(filename)

        base.set_payload(content)
        encoders.encode_base64(base)
        base.add_header('Content-disposition', 'attachment', filename=filename)

        return base

    def get_email(self):
        return input('Enter login details\nEmail: ')

    def get_password_from_user(self):
        return getpass.getpass('Enter password: ')

    def get_password_from_file(self, email):
        cred = Credentials(self.logger)
        pwd = cred.get_password(email)

        if pwd is None:
            pwd = self.get_password_from_user()

        return pwd

    def prepare_msg(self, msg_received=None, attach_file=None, edit_msg=False):
        try:

            msg = MIMEMultipart()
            empty_mail = 0

            if (msg_received is None and attach_file is None) or (edit_msg is
                    True):
                temp = tempfile.NamedTemporaryFile(suffix='task', delete=False)
                if msg_received is not None:
                    temp.write(bytes(msg_received, 'UTF-8'))
                    temp.close()
                    empty_mail = empty_mail+1
                sp.call(['vim', temp.name])
                text = open(temp.name, 'r').read()
                os.unlink(temp.name)

                msg.attach(MIMEText(text))
                if text.strip() != '':
                    empty_mail = empty_mail+1

            if edit_msg is False and msg_received is not None:
                 part = MIMEText(msg_received)
                 msg.attach(part)
                 empty_mail = empty_mail+1

            if attach_file is not None:
                if len(attach_file) is 0:
                    part = self.attach_file(None)
                    msg.attach(part)
                    empty_mail = empty_mail+1
                else:
                    for filename in attach_file:
                        part = self.attach_file(filename)
                        msg.attach(part)
                        empty_mail = empty_mail+1

            confirm = None
            if empty_mail is 0:
                confirm = input('The mail is empty, do u still wanna send'
                    '(y/n):')
                while True:
                    if confirm is 'y' or confirm is 'yes':
                        self.logger.print_log(VERBOSITY_LEVELS['info'],
                                'Sending your mail....')
                        confirm = None
                        break
                    elif confirm is 'n' or confirm is 'no':
                        self.logger.print_log(VERBOSITY_LEVELS['info'],
                                'Cancelling mail....')
                        break
                    else:
                        self.logger.print_log(VERBOSITY_LEVELS['info'],
                                'Please press y or n....')
                        confirm = input('The mail is empty, do u still wanna send'
                            '(y/n):')
                        pass


            if confirm is None:
                msg['To'] = input('Enter recipients address: ')
                msg['Subject'] = input('Give a subject: ')
                msg['From'] = self.get_email()
            else:
                msg = None

        except AttributeError:
            self.logger.print_log(VERBOSITY_LEVELS['error'], 'You are probably attaching a non MIMEText object'
                     'or there is a problem with variable name')
        return msg

