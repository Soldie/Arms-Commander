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
import re



nmap_log_dir = '/root/ArmsCommander/logs/nmap'
scan_report = str(raw_input("Enter the path for the NMap Scan Report: "))
w = open(scan_report,'r')
old_file = scan_report
new_filename = os.path.basename(old_file)
# # print colored('DEBUG: the variable NEW_FILENAME = %s','red',attrs=['bold']) % new_filename
new_file = '/root/ArmsCommander/logs/nmap/nmap_%s_parsed.txt' % new_filename
# # print colored('DEBUG: the variable NEW_FILE = %s','red',attrs=['bold']) % new_file
# # write to new file
a = open(new_file,'a')
with open(scan_report,'r') as w:
    line = w.readline()
    # sentence = line.split(line, next(line))
    sentence = str(line)
    # while line != '':
    for sentence in w:
        if re.findall('Nmap scan report for ', sentence):
            # print sentence
            sentence = sentence.replace('Nmap scan report for ','\nDNS: ')
            sentence = sentence.replace('(','\tIP: ')
            sentence = sentence.replace(')','')
            print colored('DEBUG: ' + sentence,'red',attrs=['bold'])
            # write sentence to the file
            a.write(sentence)
