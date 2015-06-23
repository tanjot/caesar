#!/usr/bin/python3

import smtplib
import getpass

def main():


    content = """Hi learning to mail the pythonic way"""

    mail = smtplib.SMTP()

    mail.connect(host='smtp.gmail.com', port=587)

    mail.set_debuglevel(True)

    mail.ehlo()

    mail.starttls()

    mail.ehlo()

    email = input('Enter login details\nEmail: ')
    password = getpass.getpass('Enter password: ')
    mail.login(email, password)

    receiver = input('Enter recipients address: ')

    mail.sendmail(email, receiver, content)

    mail.close()

if __name__ == '__main__':
    main()














