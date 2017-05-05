#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys

print colored('PASSWORD ATTACKS','cyan',attrs=['bold'])
def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Run Cylon-Raider, Interactive Menu for Aircrack-ng Replay Attacks',
        '#2. Run the Hashcat Interactive Menu Suite, including the interactive CUDA GPU driver installers'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    elif opt_Choice == "1":
        os.system('python /root/ArmsCommander/wirelessattacks/Cylon-Raider/Cylon_Raider_Main.py')
    elif opt_Choice == "2":
        os.system('python /root/ArmsCommander/passwordattacks/hashcat_suite.py')
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()
