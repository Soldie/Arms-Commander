#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
#aircrack-ng WPAcrack-01.cap -w /pentest/passwords/wordlists/darkc0de
# aircrack-ng <pcap file> -w <wordlist>

# os.system('cat /root/Cylon-Raider-Lite/banner_CrackHead.txt')
class aircrack_Parameters(object):
    def __init__(self, capture_File, path_Wordlist, found_password_file):
        self.capture_File = capture_File
        self.path_Wordlist = path_Wordlist
        self.found_password_file = found_password_file

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the location of the PCAP packet capture file that was saved by Airodump (with the 4-way handshake): ")),
            str(raw_input("Enter the path of a wordlist that you either GENERATED (with crunch) or DOWNLOADED: ")),
            str(raw_input("Enter the OUTPUT filename: "))
        )

def main():
    user_input = aircrack_Parameters.from_input()
    cmd_String = "aircrack-ng {0} -w {1} -l {2}".format(
        user_input.capture_File,
        user_input.path_Wordlist,
        user_input.found_password_file
    )
    print cmd_String
    os.system(cmd_String)
    return

main()
