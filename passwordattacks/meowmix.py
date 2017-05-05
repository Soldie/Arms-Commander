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

print colored('MEOWMIX, converts *.cap WPA2 handshake files to hashcat compatible files en-masse by wordlist','cyan',attrs=['bold'])

# hashcat_converted_dir = '/root/Documents/Easy-Suite/MeowMix'
hashcat_converted_dir = '/root/ArmsCommander/logs/HashCat'

# import wordlist as a buffer
wordlist = '/root/ArmsCommander/passwordattacks/MeowMix/wordlist'

def convert_wordlist():
    os.system('python /root/ArmsCommander/passwordattacks/MeowMix/convert.py')
    main()

def edit_wordlist():
    cmd_String = 'leafpad /root/ArmsCommander/passwordattacks/MeowMix/wordlist'
    os.system(cmd_String)
    main()
    return
def main():
    opt_list = [
        '\n\t#0. Exit to Main Menu',
        '#1. Convert wordlist',
        '#2. Edit wordlist'
    ]

    print ("\n\t".join(opt_list))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/passwordattacks/hashcat_suite.py')
    elif opt_Choice == "1":
        os.system('clear')
        convert_wordlist()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        edit_wordlist()
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()
