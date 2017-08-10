#!/usr/bin/env python
# coding=UTF-8

import os
import sys
import operator
import socket
from termcolor import colored
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import toolkits

# Dying sun fades in our sky
# The time has come for us to say goodbye
# Construct the pods, we must evacuate
# To the stars again, is this to be our fate?

def red(string):
    string = colored(string,'red',attrs=['bold'])

    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])

    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])

    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])

    return string
banner_str = """
# Dying sun fades in our sky
# The time has come for us to say goodbye
# Construct the pods, we must evacuate
# To the stars again, is this to be our fate?
"""
print red(banner_str)
# Metasploit Manual Start up Commands
print red("Starting up Metasploit services")
os.system('service postgresql start')
os.system('msfdb init')
os.system('msfdb start')
# os.chdir("/root/ArmsCommander/recon")
os.chdir('/root/ArmsCommander/PROJECT_HELLS_HORSES')

wordlist = "/root/ArmsCommander/PROJECT_HELLS_HORSES/target_list"
temp_resource_file = "/root/ArmsCommander/PROJECT_HELLS_HORSES/temp_resource_file.rc"
temp_resource_file_eject = temp_resource_file + 'eject' + '.rc'


def edit_wordlist():
    os.chdir('/root/ArmsCommander/PROJECT_HELLS_HORSES')
    os.system('echo "" > /root/ArmsCommander/PROJECT_HELLS_HORSES/target_list')
    os.system("leafpad target_list")

    return

def execute_resource_file(temp_resource_file):
    cmd_str = "msfconsole -r {0}".format(str(temp_resource_file))
    os.system(cmd_str)
    return

def read_target_list(wordlist, temp_resource_file):
    list_of_strings = "{0}".format(
        str(wordlist)
    )
    r = open(list_of_strings,'r')
    # line = r.readline()
    row_number = 1

    r = open(list_of_strings,'a+')
    with open(list_of_strings,'a+') as r:
        line = r.readline()
        sentence = str(line.strip())
        row_number = 1
        for sentence in r:
            if sentence != "":
                try:
                    w = open(temp_resource_file, 'w')
                    target_string = """

load pentest
network_discover -v -d -r {0}
exit
                    """.format(
                    str(sentence.strip())
                    )
                    w.write(target_string.strip())
                    w.close() # have to close out file
                    print red("DEBUG: Resource String written below")
                    debug_str = "cat %s" % temp_resource_file
                    os.system(debug_str)
                    prompt_str = "Now running Network Discovery + Vulnerability Database Query against: %s" % str(sentence.strip())
                    print green(prompt_str)
                    execute_resource_file(temp_resource_file)
                except:
                    print yellow("All files converted")

    return

def eject_hosts_file(temp_resource_file_eject):
    import time
    import toolkits
    os.chdir('/root/ArmsCommander/PROJECT_HELLS_HORSES')
    timestr = toolkits.get_time_string()
    hosts_file = "hosts_file_" + timestr + '.xml'
    w = open(temp_resource_file_eject, 'w')
    target_string = """

db_export -f xml {0}
exit
    """.format(
    str(hosts_file.strip())
    )
    w.write(target_string.strip())
    w.close() # have to close out file
    print red("DEBUG: Resource String written below")
    debug_str = "cat %s" % temp_resource_file_eject
    os.system(debug_str)
    prompt_str = "Exporting hosts file as: %s" % str(hosts_file.strip())
    print green(prompt_str)
    execute_resource_file(temp_resource_file_eject)

    return

def main():
    print yellow("""
    COMMANDS:

    \tRUN: Runs the Metasploit + DarkOperator Module. Uses Network Discovery to enumerate machines across a IP address range
    \tEDIT: Edit the wordlist of targets
    \tEXIT: Exit Program
    \tEJECT: Generate a exported XML database file, that can be db_imported by other Metasploit Framework Users
    """)

    opt_choice = str(raw_input(yellow("Enter a COMMAND: ")))

    if opt_choice == "RUN":
        read_target_list(wordlist, temp_resource_file)
        main()
    elif opt_choice == "EDIT":
        edit_wordlist()
        main()
    elif opt_choice == "EXIT":
        exit(0)
    elif opt_choice == "EJECT":
        eject_hosts_file(temp_resource_file_eject)
        exit(0)
    else:
        print red("You have entered a invalid option")
        main()
    return
main()
