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

wordlist = '/root/ArmsCommander/recon/MT_Recon_Wordlist'
w = open(wordlist,'r')
w = w.read()
buf = StringIO.StringIO(w)

while True:
    line = buf.readline().strip()
    if line != '':
        line = line.replace('www.','')
        line = line.replace('https://','')
        line = line.replace('http://','')
        target_URL = line # makes sure that the target_URL = NO www. or anything, just domain.gov or something
        print colored('DEBUG: TARGET URL = %s','red',attrs=['bold']) % target_URL
        line = line.replace('/','_')
        line = line.replace('(','_')
        line = line.replace(')','_')
        logfile_name = line # makes sure that logfile_name does not contain /, and instead contains _ , and no () either, which causes formatting issues
        logfile_directory = '/root/ArmsCommander/logs/multi_tool_recon'
        logfile_output = logfile_directory + '/' + logfile_name + '.txt'
        print colored('DEBUG: LOGFILE NAME = %s','red',attrs=['bold']) % logfile_output

        print colored('[+] Now Performing MT Recon on %s','green',attrs=['bold']) % target_URL
        print colored('[*] Your log file for the reconnaissance is located at %s',
            'yellow',
            attrs=['bold']
        ) % logfile_output


        # dig and nslookup is running
        print colored('[*] Running DIG and NSLookup','yellow',attrs=['bold'])
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
        print colored('Pulling WHOIS Records','yellow',attrs=['bold'])

        cmd_String = "whois {0} >> {1}".format(target_URL, logfile_output)
        os.system(cmd_String)
        print colored('[*] Pulling fierce Records','yellow',attrs=['bold'])


        cmd_String = "fierce -dns {0} >> {1}".format(target_URL, logfile_output)
        os.system(cmd_String)

        #theharvester
        print colored('Running The Harvester to search for any public emails, ALL domains, this could take a while!','yellow',attrs=['bold'])

        cmd_String = "theharvester -d {0} -l 500 -b all -h myresults.html >> {1}".format(str(target_URL), str(logfile_output))
        os.system(cmd_String)
        #Completed
        # input_file = logfile_output
        # query = ':'
        # recon_toolkits.shodan_result_splitter(input_file, query)
    else:
        print colored ('[+] COMPLETED, check {0} for your reconnaissance scans','green',attrs=['bold']).format(str(logfile_output))
        os.system('python /root/ArmsCommander/ArmsCommander.py')# New code starts here
