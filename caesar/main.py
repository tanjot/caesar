#!/usr/bin/python3

from .connection import Connection
from .mail import prepare_msg
from .mail import get_password_from_user
from .save_credential import save_email_password
from .save_credential import save_server_conf
from .save_credential import get_server_conf

import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-sc', '--add_cred',
                        help='Save username and password '
                        'in configuration file',
                        type=str
                        )

    parser.add_argument('-ss', '--server_conf',
                        help='Save SMTP server setting '
                        'of mailing client(hostname, host, port)',
                        nargs=3
                        )
    parser.add_argument('-c', '--choose_conf',
                        help='Choose configurations'
                        'for mailing client. Just give the hostname'
                        ' given while saving settings'
                        #add choices
                        )
    return parser.parse_args()

def main():

    argu = parse_args()

    conn = Connection()
    if argu.add_cred:
        save_email_password(argu.add_cred, get_password_from_user())

    else:
        host=None
        port=None

        if argu.server_conf:
            host=argu.server_conf[1]
            port=argu.server_conf[2]
            save_server_conf(argu.server_conf[0], host, port)

        elif argu.choose_conf:
            host, port=get_server_conf(argu.choose_conf)

        else:

            host, port = get_server_conf('gmail')

        if conn.create_conn(host, port) is True:
            msg = prepare_msg()
            conn.send_mail(msg)


if __name__ == '__main__':
    main()
