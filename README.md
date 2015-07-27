Caesar
======
[![Stories in Ready](https://badge.waffle.io/tanjot/caesar.png?label=ready&title=Ready)](https://waffle.io/tanjot/caesar)

A command line e-mail helper  

#Usage
Save email id and password in a configuration file. Henceforth, password for
email id  will be extracted from file itself. Don't worry about password
readibility in configuration file, it's encoded.
```sh
$:  caesar -sc abc@gmail.com
Enter password:
```

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

With caesar sending a single line mail is as easy as blinking an eye.
```sh
$:  caesar -m 'Your message here'
Enter recipients address: abc@yahoo.com
Give a subject: Subject here
Enter login details
Email: abc@gmail.com
Mail sent
```

Add all files to be attached in one go!
```sh
$:  caesar -f file1.txt file2.py
Enter recipients address: abc@yahoo.com
Give a subject: Attaching files
Enter login details
Email: abc@gmail.com
Mail sent
```

Type your message in editor along with attachments
```sh
$: caesar -f IMG.jpg -e -m 'hey'                                                                            
Enter recipients address: abc@yahoo.com
###Message opens up in vim here###
Give a subject: hi
Enter login details
Email: abc@gmail.com
Mail sent
```


This is not it, you can mix and match options according to your need. Send message
along with attachments or open an editor for typing message.
```sh
$:  caesar -m 'Your message here' -f file1 file2
```
```sh
$:  caesar -m 'Your message here' -f file1 file2 -e
```

Enjoy e-mailing!!!
