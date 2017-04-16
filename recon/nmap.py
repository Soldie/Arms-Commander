#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def main():
    opt_List = [
                '\n\t#0 Return to the main menu',
                '#1. Run a series of NMap scan, gradually increasing in intensity/intrusiveness. First with a unintrusive scan that can get past firewalls, eventually reaching a full comprehensive scan',
                '#2. Use a completely customized scan'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a scan choice: "))

    if opt_Choice == "1":
        scan_Target = str(raw_input("Either enter a specific IP address, or a entire IP address range: "))
        nmap_log_directory = '/root/ArmsCommander/logs/nmap/'
        nmap_scan_logfile = str(raw_input("What would you like to call the logfile?: "))
        nmap_logfile_fullpath = nmap_log_directory + nmap_scan_logfile
        # nmap_logfile_fullpath = str(raw_input("Enter the full path of the save file location: ")) # make it so that it autosaves in log directory
        print colored('Beginning a stealthy FIN Scan. This may be quick, depending on how many machines you are scanning. Usually gets past firewalls','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s -oN %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)
        print colored('Following up with a slightly more intrusive XMas Scan. The information returned usually is exactly the same as before','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sX -Pn -T4 -O -F --version-light --traceroute %s -oN %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)
        print colored('Now finalizing with a Comprehensive NMap scan','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default %s -oN %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)
        print colored('Scans complete, find your scans at %s','red','on_white') % nmap_logfile_fullpath
        main()
    elif opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/CustomNMap.py; exec bash\"'")
    elif opt_Choice == "0":
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
main()
