#!/usr/bin/python3

import sys
import caesar.mail

try:
    sys.exit(caesar.mail.main())
except KeyboardInterrupt:
    sys.exit(1)


