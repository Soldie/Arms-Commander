#Define execution policies
#!/usr/bin/env python
# coding=UTF-8

#import modules
import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
import recon_toolkits
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen



# def harvest_wordlist():
# ask user to provide wordlist
user_input = '/root/ArmsCommander/recon/CornHarvester_Wordlist'
wordlist = open(user_input, 'r')

# opens wordlist asnd reads each line into a variable
read_wordlist = wordlist.read()

# records line into a buffer using StringIO
buf = StringIO.StringIO(read_wordlist)

#while loop for each line

while True:
    line = buf.readline().strip()
    if line != "":
    # makes variable for a file containing the harvest of the domain
        line.replace('http://www.','')
        line.replace('https://www.','')
        line.replace('/','')
        log_directory = '/root/ArmsCommander/logs/CornHarvester/'
        harvest_file = line + '_harvest.txt'
        # sets the harvester command string
        # print colored('Now harvesting emails for %s','red','on_white') % line
        print colored('[*] Now harvesting emails for %s','yellow',attrs=['bold']) % line
        # makes harvest file
        # command string
        save_filename = line
        save_filename = save_filename.replace('http://www.','')
        save_filename = save_filename.replace('https://www.','')
        save_filename = save_filename.replace('/','')
        save_file = log_directory + save_filename + '.txt'
        cmd_String = "theharvester -d %s -l 500 -b all -h myresults.html >> %s" % (line, save_file)
        # cmd_String = "theharvester -d %s -l 500 -b all >> /root/ArmsCommander/logs/CornHarvester/%s/%s" % (line, domain_directory, harvest_file)
        # prints a copy of the command string for debugging purposes
        print colored(cmd_String,'red','on_white')
        # runs the command string
        os.system(cmd_String)
        # print colored('Completed harvest of %s','blue','on_white') % line
        print colored('Completed harvest of %s','green',attrs=['bold']) % line
        recon_toolkits.cornharvester_to_csv(save_file)
        # except buf == "":
        #     print 'Reached end of line of wordlist'
        #     pass
    else:
        print 'Reached end of line of your wordlist'
        print 'Please check /root/ArmsCommander/logs/CornHarvester/ for your results'
        print 'ENDING PROGRAM'
        exit(0)
