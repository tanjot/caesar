Caesar
======
[![Stories in Ready](https://badge.waffle.io/tanjot/caesar.png?label=ready&title=Ready)](https://waffle.io/tanjot/caesar)

A command line mail helper  
Yeah, that's how you spell caesar!  

#Usage
Save email id and password in a configuration file. Henceforth, password for
email id  will be extracted from file itself. 
```sh
$:  caesar -sc charmingtanjot
```
Enter password:

Save server settings, IP and port number to send mail using the mailing client. The first value given eg: 'ymail' in
following sample will be used henceforth for referring the server's settings.
```sh
$:  caesar -ss ymail smtp.mail.yahoo.com 587  
```

To further use this server settings for mailing,
```sh
$:  caesar -c ymail
```
This will allow sending mail using a yahoo email id

Sending a small single line mail is as easy as blinking.
```sh
$:  caesar -m 'Your message here'
Enter recipients address: abc@yahoo.com
Give a subject: Subject here
Enter login details
Email: abc@gmail.com
Mail sent
```

Add all file to be attached in one go!!!
```sh
$:  caesar -f file1.txt file2.py
Enter recipients address: abc@yahoo.com
Give a subject: Attaching files
Enter login details
Email: abc@gmail.com
Mail sent
```


There's more to it, mix and match the options according to need. Send message
along with attching files.
```sh
$:  caesar -m 'Your message here' -f file1 file2
```
