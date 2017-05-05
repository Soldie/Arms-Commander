#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable
import os
import sys
import operator
from termcolor import colored

def boost_mode():
    os.system('nvidia-smi -pm 1')
    os.system('nvidia-smi -e 1')
    os.system('nvidia-smi -ac 960,1124')
    os.system('nvidia-smi --auto-boost-permission=0')
    os.system('nvidia-smi --auto-boost-default=1')
    print colored('[*] Clock set to 1124 mhz GPU, 960 mhz memory','yellow',attrs=['bold'])
    main()
    return

def monitor_systems():
    cmd_String = "gnome-terminal -e 'bash -c \"nvidia-smi dmon; exec bash\"'"
    os.system(cmd_String)
    cmd_String = "gnome-terminal -e 'bash -c \"nvidia-smi stats; exec bash\"'"
    os.system(cmd_String)
    print colored('[*] All monitoring modes enabled','yellow',attrs=['bold'])
    return

def main():
    print colored('MAIN MENU','cyan',attrs=['bold'])
    opt_List = [
        '\n\t#0. Exit Program',
        '#1. Set my video card to full constant-boost mode, at 1124 mhz GPU clock, 960 mhz memory clock',
        '#2. Activate all monitoring systems'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))


    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        boost_mode()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        monitor_systems()
        main()
main()
