#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# New code starts here

# ask user who to scan
target_URL = str(raw_input("Enter the URL/Host you want to perform recon on: "))
# ask user what to call logfile
logfile_name = str(raw_input("What would you like to name your logfile?: "))
# logfile main directory

logfile_directory = '/root/ArmsCommander/logs/multi_tool_recon'
logfile_output = logfile_directory + '/' + logfile_name + '.txt'

print colored('Your log file for the reconnaissance is located at %s','blue','on_white') % logfile_output
print colored('Scans Commencing, Do Not Interrupt until Completed! (The command prompt tells you completed)','red','on_white')

# dig and nslookup is running
print colored('Running DIG and NSLookup','red','on_white')
cmd_String = "dig {0} >> {1}".format(
                            str(target_URL),
                            str(logfile_output)
                            )
os.system(cmd_String)
cmd_String = "nslookup {0} >> {1}".format(
                            str(target_URL),
                            str(logfile_output)
                            )
os.system(cmd_String)
print colored('Pulling WHOIS Records','red','on_white')

cmd_String = "whois {0} >> {1}".format(target_URL, logfile_output)
os.system(cmd_String)
print colored('Pulling fierce Records','red','on_white')
cmd_String = "fierce -dns {0} >> {1}".format(target_URL, logfile_name)
os.system(cmd_String)

#theharvester
print colored('Running The Harvester to search for any public emails, ALL domains, this could take a while!','red','on_white')
cmd_String = "theharvester -d {0} -l 500 -b all -h myresults.html >> {1}".format(str(target_URL), str(logfile_name))
os.system(cmd_String)
#Completed
print colored ('COMPLETED, check {0} for your reconnaissance scans','red','on_blue').format(str(logfile_name))
os.system('python /root/ArmsCommander/ArmsCommander.py')
