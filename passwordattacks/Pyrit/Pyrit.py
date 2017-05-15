import os
import socket
import sys
import StringIO
from termcolor import colored
import time
import subprocess
import operator

capture_wordlist = '/root/ArmsCommander/passwordattacks/Pyrit/wordlist'
logfile_dir = '/root/ArmsCommander/logs/Pyrit'

def read_wordlist(): # Here you should say, readlines of wordlist and save to a buffer
    os.system('python /root/ArmsCommander/passwordattacks/Pyrit/read_wordlist.py')
    main()


def edit_wordlist():
    os.system('leafpad /root/ArmsCommander/passwordattacks/Pyrit/wordlist')
    main()
    return

def output_hashes(logfile_dir):
    # cmd_String = 'cat %s/*' % logfile_dir
    cmd_String = 'nautilus %s' % logfile_dir
    os.system(cmd_String)
    main()
    return

def main():

    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Read the files in the wordlist, analyze the hash through Pyrit, and create a logfile on unique keys found',
        '#2. Edit the wordlist',
        '#3. Output the found hashes'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    elif opt_Choice == "1":
        os.system('clear')
        read_wordlist()
    elif opt_Choice == "2":
        edit_wordlist()
    elif opt_Choice == "3":
        os.system('clear')
        output_hashes(logfile_dir)
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
