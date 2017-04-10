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
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# Banner Page
os.system('cat /root/ArmsCommander/banner_cornharvester.txt')
# Intro Page
# # Rain makes corn, corn makes whiskey / Whiskey makes my baby, feel a little frisky

print '\n\tRain makes corn'
print '\tCorn makes whiskey'
print '\tWhiskey makes my baby...'
print '\tFeel a little frisky'
print "\n\t'Rain is a Good Thing' by Luke Bryan"
# ask user to provide wordlist
user_input = str(raw_input("Enter a wordlist file of domains containing 'example.com' on each line: "))
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
        log_directory = '/root/ArmsCommander/logs/CornHarvester/'
        harvest_file = line + '_harvest.txt'
        # sets the harvester command string
        print colored('Now harvesting emails for %s','red','on_white') % line
        # makes harvest file
        # command string
        cmd_String = "theharvester -d %s -l 500 -b all -h myresults.html >> %s%s" % (line, log_directory, harvest_file)
        # cmd_String = "theharvester -d %s -l 500 -b all >> /root/ArmsCommander/logs/CornHarvester/%s/%s" % (line, domain_directory, harvest_file)
        # prints a copy of the command string for debugging purposes
        print colored(cmd_String,'red','on_white')
        # runs the command string
        os.system(cmd_String)
        print colored('Completed harvest of %s','blue','on_white') % line
        # except buf == "":
        #     print 'Reached end of line of wordlist'
        #     pass
    else:
        print 'Reached end of line of your wordlist'
        print 'Please check /root/ArmsCommander/logs/CornHarvester/ for your results'
        print 'ENDING PROGRAM'
        exit(0)

#
# results = []
# with open('/root/Documents/domainsRelatedToNiantic', 'r') as inputFile:
#     for line in inputFile:
#         results.append(line.strip().split(',')) # this basically fills the list "results" three lienes back up
# # convert each line of wordlist into a set
#     for line in results:
#         line = line.replace('"', "")
#         line = line.replace("'", "")
#         line = line.split("=")
# # Run commands against the set using theharvester
#         # theharvester -d microsoft.com -l 500 -b google -h myresults.html
#     cmd_String = "theharvester -d %s -l 500 -b all" % line
#     print cmd_String
#     os.system(cmd_String)
