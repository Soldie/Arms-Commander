#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time
# from Cylon_Raider_Main import capture_Interface
import Cylon_Raider_Main.py



def start_targeted_capture(capture_BSSID, capture_Channel):
    print 'Beginning targeted capture'
    timestr = (time.strftime("%Y%m%d-%H%M%S"))
    # make it so that I create a folder with that same instance of handshake capture
    airodump_capture_filepath = "/root/Cylon-Raider-Lite/logs/"
    airodump_capture_folder = airodump_capture_filepath + capture_BSSID + '/'
    make_Folder_String = "mkdir {0}".format(airodump_capture_folder)
    os.system(make_Folder_String)
    airodump_capture_file = airodump_capture_folder + timestr + ".cap"
    cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
        capture_BSSID,
        capture_Channel,
        airodump_capture_file,
        capture_Interface
    )
    print cmd_String
    os.system(cmd_String)
    return capture_BSSID, capture_Channel, airodump_capture_file, capture_Interface
def gather_targeted_info():
    capture_BSSID = str(raw_input("Enter the BSSID of AP TARGET: "))
    capture_Channel = str(raw_input("Enter the CHANNEL of AP TARGET: "))
    start_targeted_capture(capture_BSSID, capture_Channel)
    return capture_BSSID, capture_Channel


def main():
    gather_targeted_info()
    return
main()
