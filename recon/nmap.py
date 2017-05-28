#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import recon_toolkits
import time
# IP_wordlist = str('NULL')



def single_scan():

        timestr = time.strftime("%Y%m%d-%H%M%S")
        scan_Target = str(raw_input("Either enter a specific IP address, or a entire IP address range: "))
        nmap_log_directory = '/root/ArmsCommander/logs/nmap/'
        nmap_scan_logfile = str(raw_input("What would you like to call the logfile?: "))
        nmap_logfile_fullpath = nmap_log_directory + nmap_scan_logfile
# needed for the new module to work

        # target = scan_Target
        # nmap_output_file = nmap_logfile_fullpath


        # nmap_logfile_fullpath = str(raw_input("Enter the full path of the save file location: ")) # make it so that it autosaves in log directory
        print colored('Beginning a stealthy FIN Scan. This may be quick, depending on how many machines you are scanning. Usually gets past firewalls','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s >> %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)

        # target = scan_Target
        # nmap_output_file = nmap_logfile_fullpath
        # recon_toolkits.nmap_log_to_csv(timestr, nmap_cmd_string, scan_Target, nmap_logfile_fullpath)
        recon_toolkits.nmap_log_to_csv(timestr, nmap_cmd_string, scan_Target, nmap_logfile_fullpath)

        print colored('Following up with a slightly more intrusive XMas Scan. The information returned usually is exactly the same as before','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -v -O -sX -Pn -T4 -O -F --version-light --traceroute %s >> %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)


        # target = scan_Target
        # nmap_output_file = nmap_logfile_fullpath
        recon_toolkits.nmap_log_to_csv(timestr, nmap_cmd_string, scan_Target, nmap_logfile_fullpath)

        print colored('Now finalizing with a Comprehensive NMap scan','red','on_white')
        nmap_cmd_string = "sudo proxychains nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script default %s >> %s" % (scan_Target, nmap_logfile_fullpath)
        print colored(nmap_cmd_string,'red','on_white')
        os.system(nmap_cmd_string)
        logfile_cmd_string = (nmap_cmd_string + ' >> ' + '%s' + '_logfile') % nmap_logfile_fullpath
        os.system(logfile_cmd_string)

        # target = scan_Target
        # nmap_output_file = nmap_logfile_fullpath
        recon_toolkits.nmap_log_to_csv(timestr, nmap_cmd_string, scan_Target, nmap_logfile_fullpath)

        print colored('Scans complete, find your scans at %s','red','on_white') % nmap_logfile_fullpath


        main()
        return

def main():
    opt_List = [
                '\n\t#0 Return to the main menu',
                '#1. Run a series of NMap scan, gradually increasing in intensity/intrusiveness. First with a unintrusive scan that can get past firewalls, eventually reaching a full comprehensive scan',
                '#2. Use a completely customized scan',
                '#3. Run a wordlist scan with supplied wordlist of IP addresses',
                '#4. Scan IP addresses for vulnerable services, and write to a csv file',
                '#5. Attempt to bruteforce common protocols such as SSH, Telnet, and FTP, via a wordlist and THC Hydra'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a scan choice: "))
    print colored('DEBUG: Choice selected #%s','red',attrs=['bold']) % opt_Choice
    if opt_Choice == "1":
        single_scan()
    elif opt_Choice == "2":
        os.system("gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/recon/CustomNMap.py; exec bash\"'")
    elif opt_Choice == "3":
        # wordlist_scan() # do not type return here!
        # wordlist = str(raw_input("Enter the full path of a wordlist containing IP addresses: "))
        os.system('python /root/ArmsCommander/recon/nmap_wordlist_scan.py')
    elif opt_Choice == "4":
        wordlist = str(raw_input("Enter the PATH to a wordlist of IP addresses: "))
        recon_toolkits.nmap_read_wordlist(wordlist)
    elif opt_Choice == "5":
        protocol = str(raw_input("What protocol are you bruteforcing? (e.g. 'ssh', 'ftp',etc): "))
        ip_list = str(raw_input("Enter the PATH to a wordlist of HOSTS (IP addresses): "))
        username_list = str(raw_input("Enter the PATH to a wordlist of USERNAMES: "))
        password_list = str(raw_input("Enter the PATH to a wordlist of PASSWORDS: "))

        recon_toolkits.hydra_ip_list(username_list, password_list, ip_list, protocol)
    elif opt_Choice == "0":
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
main()
