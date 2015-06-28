#!/usr/bin/python3

from .connection import Connection
from .mail import prepare_msg
from .mail import get_email
from .mail import get_password_from_user
from .save_credential import save_email_password
from colorama import Fore

import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--add_cred',
                        help='Save username and password '
                        'in configuration file',
                        type=str
                        )

    return parser.parse_args()

def main():

    argu = parse_args()

    if argu.add_cred:
        save_email_password(argu.add_cred, get_password_from_user())
    else:

        conn = Connection()
        conn.create_conn()
        msg = prepare_msg()
        conn.send_mail(msg)


if __name__ == '__main__':
    main()