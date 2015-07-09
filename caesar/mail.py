#!/usr/bin/python3

import getpass

from .logger import Logger
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from .save_credential import Credentials
from .utils import Utils

utils = Utils()
input = utils.input_for_python_2_3()

class Mail():

    def __init__(self, logger):
        self.logger = logger

    def read_data_from_file(self):
        filename = input('Enter file to read data: ')

        fhan = open( filename, 'rb')

        content = fhan.read()
        fhan.close()
        return content, filename


    def attach_file(self):
        base = MIMEBase('application', "octet-stream")
        content, filename = self.read_data_from_file()

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

    def prepare_msg(self):
        msg = MIMEMultipart()
        #msg = MIMEText(read_data_from_file())

        msg.attach(self.attach_file())
        msg['To'] = input('Enter recipients address: ')
        msg['Subject'] = input('Give a subject: ')
        msg['From'] = self.get_email()

        return msg

