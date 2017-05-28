#!/usr/bin/env python
# coding=UTF-8

# NOT WORKING ight now

import os
import socket
import operator
# #from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

print 'All this does is run Aircrack-ng without a specified wordlist (therefore it will fail to run) but instead it will tell you which *.cap files have the handshake'

directory = '/root/Cylon-Raider-Lite/logs/'
files = str(os.listdir(directory))

if os.path.isfile(files) and files.endswith(".cap"):
    cmd_String = 'aircrack-ng %s' % files
    os.system(cmd_String)
else:
    print 'Finished checking all *.cap files'
