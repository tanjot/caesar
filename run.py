#!/usr/bin/python3

import sys
import caesar.main

try:
    sys.exit(caesar.main.main())
except KeyboardInterrupt:
    sys.exit(1)


