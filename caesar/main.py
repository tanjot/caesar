#!/usr/bin/python3

from .connection import Connection
from .mail import prepare_msg
from colorama import Fore


def main():
    conn = Connection()
    conn.create_conn()
    msg = prepare_msg()
    conn.send_mail(msg)


if __name__ == '__main__':
    main()
