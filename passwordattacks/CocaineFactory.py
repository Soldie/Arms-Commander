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

print colored('CRACK COCAINE FACTORY, \nthe automated password-hasher for Hashcat GPU cracking rigs\nBy Chang Tan Lister\nwww.github.com/tanc7','white',attrs=['bold'])

# Cocaine Factory mass-cracks via hashcat GPU utilization
# Simply go by a wordlist, and submit it to this program and it'll do the rest

user_input = '/root/ArmsCommander/passwordattacks/CocaineFactory/wordlist'
w = open(user_input,'r')
read_w = w.read()
buf = StringIO.StringIO(read_w)
# wordlist_file = '/media/root/Data/WifiPasswordMegafile.txt' # Default wordlist weighing at about 15 gigabytes of single lines of data
wordlist_file = str(raw_input("Enter the FULL PATH of your PASSWORD DICTIONARY: "))

while True:
    line = buf.readline().strip()
    if line != '':
        line = line.replace('(','\(')
        line = line.replace(')','\)')
        hash_file = line
        print colored('[+] Now cracking the hashes of file: %s','yellow',attrs=['bold']) % hash_file
        cmd_String = 'hashcat -a 0 -w 4 -m 2500 %s %s' % (hash_file, wordlist_file)
        os.system(cmd_String)
    else:
        print colored('[-] Hashcat has finished going through the wordlists you provided against your password dictionary\nPlease Check the console output for results','red',attrs=['bold'])
        exit(0)
