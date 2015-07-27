#!/usr/bin/python3

from .connection import Connection

from .logger import Logger
from .logger import VERBOSITY_LEVELS
from .mail import Mail
from .save_credential import Credentials

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

    parser.add_argument('-v', '--verbosity',
                        help='Level of viewing logs: 1. Only info, '
                        '2.Errors and Info, 3. Trace of all request '
                        'and reply messages',
                        type=int,
                        choices=range(1, 4)
                        )

    parser.add_argument('-m', '--msg',
                        help='Type message to be sent inside quotes',
                        type=str
                        )

    parser.add_argument('-f', '--file',
                        help='Attach file with mail',
                        type=str,
                        nargs='*'
                        )

    parser.add_argument('-e', '--edit',
                        help='Type msg in editor',
                        action='store_true'
                        )

    return parser.parse_args()

def main():

    argu = parse_args()


    if argu.verbosity is None:
        argu.verbosity = 1

    logger = Logger(argu.verbosity)

    conn = Connection(logger)
    cred = Credentials(logger)
    mail = Mail(logger)

    if argu.add_cred:
        if cred.check_email_exists(argu.add_cred) is False:
            cred.save_email_password(argu.add_cred,  mail.get_password_from_user())
            logger.print_log(VERBOSITY_LEVELS['info'], 'Successfully saved '
                'email and password')
        else:
            logger.print_log(VERBOSITY_LEVELS['info'], 'Email ID already'
                'exists')
    elif argu.server_conf:
        host_name = argu.server_conf[0]
        host=argu.server_conf[1]
        port=argu.server_conf[2]

        if cred.check_server_exists(host_name) is False:
            cred.save_server_conf(host_name, host, port)
            logger.print_log(VERBOSITY_LEVELS['info'], 'Successfully saved '
                    'server settings')
        else:
            logger.print_log(VERBOSITY_LEVELS['info'], 'Server settings already'
                'exists')
    else:
        host=None
        port=None


        if argu.choose_conf:
            host, port = cred.get_server_conf(argu.choose_conf)

        else:

            host, port = cred.get_server_conf('gmail')

        if conn.create_conn(host, port) is True:
            msg = mail.prepare_msg(argu.msg, argu.file, argu.edit)
            if msg is not None and conn.send_mail(msg) is True:
                logger.print_log(VERBOSITY_LEVELS['info'], 'Mail sent')

    return 0


if __name__ == '__main__':
    main()
