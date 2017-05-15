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


# hashcat_converted_dir = '/root/Documents/Easy-Suite/MeowMix'
hashcat_converted_dir = '/root/ArmsCommander/logs/HashCat'

# import wordlist as a buffer
wordlist = '/root/ArmsCommander/passwordattacks/MeowMix/wordlist'

# read wordlist
w = open(wordlist, 'r')
read_w = w.read()
buf = StringIO.StringIO(read_w)

# for each line that ends with *.cap in wordlist, run aircrack-ng -J %s/directory
while True:
    line = buf.readline().strip()
    if line != "":
        line = line.replace('(','\(')
        line = line.replace(')','\)')
        original_name = os.path.basename(line)
        print colored('[+] Now converting %s to hashcat compatible format','green',attrs=['bold']) % original_name
        # cmd_String = 'aircrack-ng %s %s/hashcat_%s' % (line, hashcat_converted_dir, original_name)
        cmd_String = 'cap2hccapx.bin %s %s/hashcat_%s.hccapx' % (line, hashcat_converted_dir, original_name)
        print cmd_String
        os.system(cmd_String)
    else:
        print colored('Conversion to hashcat format completed, see %s for your results','green',attrs=['bold']) % hashcat_converted_dir
        os.system('python /root/ArmsCommander/passwordattacks/meowmix.py')
