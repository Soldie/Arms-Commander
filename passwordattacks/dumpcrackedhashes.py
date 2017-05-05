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

hashfile_dir = '/root/ArmsCommander/logs/HashCat'
log_dir = '/root/ArmsCommander/logs/HashCat'

print colored('Note: The wordlist for this is shared with your "CocaineFactory wordlist"','white',attrs=['bold'])
wordlist_hashes = '/root/ArmsCommander/passwordattacks/CocaineFactory/wordlist'
w = open(wordlist_hashes,'r')
read_w = w.read()
buf = StringIO.StringIO(read_w)
while True:
    line = buf.readline().strip()
    if line != "":
        line = line.replace('(','\(')
        line = line.replace(')','\)')
        hashfile_original = line
        output_file = os.path.basename(hashfile_original)
        # cmd_String = "hashcat -m 2500 --show -o %s/HashCat_Dump_%s.txt %s" % (log_dir, output_file, hashfile_original) # you have to specify the hash format! Otherwise it errors out, so if its a WPA2 password, then you gotta do -m 2500 exactly
        cmd_String = "hashcat -m 2500 --show %s" % hashfile_original
        print colored('[*] Now outputting hashes for hashfile %s','yellow',attrs=['bold']) % hashfile_original
        print colored(cmd_String,'green',attrs=['bold'])
        os.system(cmd_String)
    else:
        print colored('[+] Finished dumping hashes','green',attrs=['bold'])
        print colored('[!] Your dumped hashes is located at %s','red',attrs=['bold']) % log_dir
        os.system('python /root/ArmsCommander/passwordattacks/hashcat_suite.py')
