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

os.system('cat /root/Cylon-Raider-Lite/banner_CrackHead.txt')

# Elimiante the classes
# class aircrack_Parameters(object):
#     def __init__(self, capture_File, path_Wordlist):
#         self.capture_File = capture_File
#         self.path_Wordlist = path_Wordlist
#
#     @classmethod
#     def from_input(cls):
#         return cls(
#             str(raw_input("Enter the location of the PCAP packet capture file that was saved by Airodump (with the 4-way handshake): ")),
#             str(raw_input("Enter the path of a wordlist that you either GENERATED (with crunch) or DOWNLOADED: "))
#         )

def main():
    # user_input = aircrack_Parameters.from_input()

    # Thats so weird, this doesnt even work either. It's something wrong with the syntaxc of aircrack?
    # Okay, tested the syntaxc
    # so Aircrack-ng's syntax, for output file -o does NOT support a full directory specified. It only supports the CURRENT directory to output to

    # nope doenst work either
    os.system('cd /root/Cylon-Raider-Lite/logs/FOUND_PASSWORDS') # that means this is the solution, automatically navigating the terminal to the desired directory
    capture_File = str(raw_input("Enter the CAPTURE FILE path: "))
    path_Wordlist = str(raw_input("Enter the WORDLIST path: "))
    found_password_file = str(raw_input("Name your OUTPUT file: "))
    # it still saves it in the current directory of the user. That is really weird
    # Aircrack uses it's own unique "GUI", where it runs through several thousand hashes per second, that may be why

    # cannot even prepend a directory change. Alright, i'll just leave that out of the release

    # found_password_folder = '/root/Cylon-Raider-Lite/logs/FOUND_PASSWORDS/'
    # found_password_path = found_password_folder + found_password_file + '.txt'

    # Okay, tested the syntaxc
    # so Aircrack-ng's syntax, for output file -o does NOT support a full directory specified. It only supports the CURRENT directory to output to

    # This doesnt work for some reason
    # found_password_filename = user_input.capture_File
    # found_password_file = found_password_filename + '.txt'
    # found_password_folder = '/root/Cylon-Raider-Lite/logs/FOUND_PASSWORDS/'
    # found_password_path = found_password_folder + found_password_file

    # Neither does this but I will just leave this code in
    # found_password_filename = str(user_input.capture_File)
    # found_password_path = found_password_filename + '.txt'
    cmd_String = "aircrack-ng {0} -w {1} -l {2}".format(
        capture_File,
        path_Wordlist,
        found_password_file
    )
    print cmd_String
    os.system(cmd_String)
    return

main()
