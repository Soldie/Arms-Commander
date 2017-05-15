#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
#from nmap import * # this was causing problems. Because this would import all variables
# from nmap import wordlist # import just wordlist variable
# from now on just make a separate python script that collects the variables
import StringIO

wordlist = str(raw_input("Enter the full path of a wordlist containing IP addresses: "))

w = open(wordlist,'r')
w = w.read()
buf = StringIO.StringIO(w)
logfile_directory = '/root/ArmsCommander/logs/nmap'
while True:
    line = buf.readline().strip()
    if line != '':
        line = buf.readline().strip()
        target_IP = line
        line = line.replace('/','_whole_range_')
        save_file = '%s/%s/%s_nmap.txt' % (logfile_directory, line, line)
        print colored('[+] Now scanning IP Address: %s','magenta',attrs=['bold']) % target_IP
        cmd_String = 'mkdir %s/%s' % (str(logfile_directory), str(line))
        os.system(cmd_String)
        # os.system('mkdir %s/%s') % (str(logfile_directory), str(target_IP))
        cmd_String = "sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s >> %s" % (target_IP, save_file)
        print colored('Running FIN scan against %s','yellow',attrs=['bold']) % target_IP
        os.system(cmd_String)
        cmd_String = "sudo proxychains nmap -v -O -sX -Pn -T4 -O -F --version-light --traceroute %s >> %s" % (target_IP, save_file)
        os.system(cmd_String)
        print colored('[*] Now running XMAS scan against %s','yellow',attrs=['bold']) % target_IP
        cmd_String = "sudo proxychains nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default %s >> %s" % (target_IP, save_file)
        os.system(cmd_String)
        print colored('[*] Now running Comprehensive Scan against %s','yellow',attrs=['bold']) % target_IP
        print colored('[*] Completed scan against: %s','green',attrs=['bold']) % target_IP
    else:
        os.system('python /root/ArmsCommander/recon/nmap.py')

# I should have made a get_var.py module, so basically to call upon the variable of X. it would be.
#
# /$path/get_var.py
# import stuff
#
# def get_var_variable():
#     variable = stuff
    # return variable
#
# /$path/Program.py
#
# from get_var import variable (avoid using * because then it'll ask all the questions again)
#
# var = get_var.variable
