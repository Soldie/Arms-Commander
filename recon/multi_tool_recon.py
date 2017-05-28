#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
import recon_toolkits
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# New code starts here
logfile_directory = '/root/ArmsCommander/logs/multi_tool_recon'

def single_recon():
    # ask user who to scan
    target_URL = str(raw_input("Enter the URL/Host you want to perform recon on: "))
    # ask user what to call logfile
    logfile_name = str(raw_input("What would you like to name your logfile?: "))
    # logfile main directory

    logfile_directory = '/root/ArmsCommander/logs/multi_tool_recon'
    logfile_output = logfile_directory + '/' + logfile_name + '.txt'


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


    cmd_String = "fierce -dns {0} >> {1}".format(target_URL, logfile_name)
    os.system(cmd_String)

    #theharvester
    print colored('Running The Harvester to search for any public emails, ALL domains, this could take a while!','yellow',attrs=['bold'])

    cmd_String = "theharvester -d {0} -l 500 -b all -h myresults.html >> {1}".format(str(target_URL), str(logfile_name))
    os.system(cmd_String)
    #Completed
    print colored ('[+] COMPLETED, check {0} for your reconnaissance scans','green',attrs=['bold']).format(str(logfile_output))
    # input_file = logfile_output
    # query = ':'
    # recon_toolkits.shodan_result_splitter(input_file, query)
    cmd_String = 'cat %s' % logfile_output
    os.system(cmd_String)

    main()
    return

def start_wordlist_recon():
    os.system('python /root/ArmsCommander/recon/multi_tool_by_wordlist.py')
    main()
    return

def edit_wordlist_recon():
    cmd_String = 'leafpad /root/ArmsCommander/recon/MT_Recon_Wordlist'
    os.system(cmd_String)
    return

def wordlist_recon():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Start wordlist recon',
        '#2. Edit the targeted hosts wordlist'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('python /root/ArmsCommander/recon/multi_tool_recon.py')
    elif opt_Choice == "1":
        start_wordlist_recon()
        wordlist_recon()
    elif opt_Choice == "2":
        os.system('clear')
        edit_wordlist_recon()
        wordlist_recon()
    else:
        print colored('You have entered an invalid option','red',attrs=['bold'])
        wordlist_recon()
    return

def dump_data(search_term, logfile_directory):
    cmd_String = 'cat %s/*%s*' % (logfile_directory, search_term)
    os.system(cmd_String)
def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. MT Recon a Single Host',
        '#2. MT Recon Multiple Hosts by wordlist',
        '#3. Dump all harvested data that matches a term',
        '#4. Organize SHODAN entries of MT Recon files by Hostname and IP'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ArmsCommander/ArmsCommander.py')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        single_recon()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        wordlist_recon()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        search_term = str(raw_input("Enter a search term: "))
        dump_data(search_term, logfile_directory)
        main()
        return search_term
    elif opt_Choice == "4":
        os.system('clear')
        MT_file = str(raw_input("Multi-Tool-Recon Output file location: "))
        # recon_toolkits.shodan_result_splitter(str(raw_input("Enter the location of your multi-tool-recon file: "))
        recon_toolkits.cornharvester_to_csv(MT_file)
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()
