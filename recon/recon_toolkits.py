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
import time

def convert_cornharvester_to_dmitry():
    ch_log_dir = '/root/ArmsCommander/logs/CornHarvester'
    hosts_file = '/root/ArmsCommander/logs/dmitry/all_hosts.csv'
    cmd_String = 'rm -rf %s' % hosts_file
    os.system(cmd_String)
    print colored('Changing directory to CornHarvester to process logfiles into Dmitry Compatible Format','yellow',attrs=['bold'])
    os.chdir(ch_log_dir)
    cmd_String = 'cat *hosts* >> /root/ArmsCommander/logs/dmitry/all_hosts.csv'
    os.system(cmd_String)
    print colored('Sending file to Dmitry for processing','yellow',attrs=['bold'])
    dmitry_processor(hosts_file)
    return hosts_file

def dmitry_processor(hosts_file):
    # read lines
    r = open(hosts_file,'r')
    with open(hosts_file,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
    #and gets rid of the following useless information
        for sentence in r:
            # determines whether the line contains either a IP address or a DNS or hostname
            if re.findall('.',sentence):
                try:
                    sentence = str(sentence)
                    sentence = sentence.replace('[+] Emails found,','')
                    sentence = sentence.replace('[+] Hosts found in search engines,','')
                    sentence = sentence.replace('[+] Virtual hosts,','')
                    sentence = sentence.replace('[+] Shodan Database search,','')
                    sentence = sentence.replace('Searching for,','')
                    sentence = sentence.replace('\n','')
                    sentence = sentence.strip()
                    sentence = sentence.split(',')
                    hostname = sentence[1]
            # writes the modified lines into a new file
                    hosts_file = os.path.basename(hosts_file)
                    processed_hosts_file = '/root/ArmsCommander/logs/dmitry/%s_processed.csv' % hosts_file
                    print colored('Writing to new Dmitry file','yellow',attrs=['bold'])
                    write_string = str(hostname) + '\n'
                    w = open(processed_hosts_file,'a+')
                    w.write(write_string)
                    w.close()
                    print colored('Your processed hosts file is: %s','yellow',attrs=['bold']) % processed_hosts_file
                except IOError:
                    pass
                except IndexError:
                    pass
    # closes the file and sends it to reader
        print colored('Loading processed hosts file into Dmitry for detailed scanning','yellow',attrs=['bold'])
        dmitry_reader(processed_hosts_file)
    return processed_hosts_file

def dmitry_reader(processed_hosts_file):
    r = open(processed_hosts_file,'r')
    with open(processed_hosts_file,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        for sentence in r:
            try:
                target = sentence
                print colored(target,'yellow',attrs=['bold'])
                print colored('Now scanning with Dmitry: %s','yellow',attrs=['bold']) % target
                dmitry_scanner(target)
            except IOError:
                pass
    return

def dmitry_scanner(target):

    hostname = target
    dmitry_output_file = target + '_dmitry.csv'
    # dmitry doenst seem to support backslashes in its syntax, like to specify that it goes into the ArmsCommander directory

    dmitry_dir = '/root/ArmsCommander/logs/dmitry'

    # dmitry_output = dmitry_dir + '/' + dmitry_output_file
    os.chdir(dmitry_dir) # we can force the terminal to change directory to dmitry dir  to compensate so that everying is saved there

    cmd_String = "dmitry -winsepo %s %s" % (dmitry_output_file, target)
    cmd_String = cmd_String.replace('\n','')
    print colored(cmd_String,'red',attrs=['bold'])
    os.system(cmd_String)

    return


def debug_text(text_display):
    print colored('DEBUG PROMPT: ' + text_display,'red',attrs=['bold'])
    return
def nmap_parser(wordlist):
    nmap_log_dir = '/root/ArmsCommander/logs/nmap'
    scan_report = wordlist
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
                # print colored('DEBUG: ' + sentence,'red',attrs=['bold'])
                # write sentence to the file
                a.write(sentence)
    return new_file

def read_wordlist_into_buffer(wordlist):
    return

def write_file(option, writeto):
    return

def color_text(input, color, features):
    return colored_text

def text_formatter(query, replace, replacewith, split):
    return formatted_text

def shodan_result_splitter(input_file):
    query = ':'
    # debug_string = 'Now starting splitter on input file: ' + str(input_file) ' with query: ' + str(query)
    # debug_text(debug_string)
    # time.sleep(5)
    shodan_log_dir = '/root/ArmsCommander/logs/multi_tool_recon/'
    # input_file is imported from the main modules
    r = open(input_file,'r')
    # debug_text('Shodan file opened')
    with open(input_file,'r') as r:
        line = r.readline()
        sentence = str(line)
        for sentence in r:
            if re.findall(query, sentence):
                sentence = sentence.split(query)
                # debug_string = 'Sentence split based upon query: ' + query
                # debug_text(debug_string)
                ip_addr = sentence[0]
                host_addr = sentence[1]
                # write both data values to separate files or separate lines
                write_filename = os.path.basename(input_file)
                write_file = shodan_log_dir + write_filename + '_split' + '.txt'
                w = open(write_file,'a')
                # debug_text('Write file opened')
                w.write('\n' + host_addr) # write separate line for host address if known
                w.write('\n' + ip_addr) # write separate line for IP address if known
                w.write('\n-----------------------------') # draws a boundary to indicate separate entities in writefile
                # debug_text('Write file entries written')
                w.close()
    return ip_addr, host_addr, write_file
        # nmap_cmd_string = "sudo sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s -oN %s" % (scan_Target, nmap_logfile_fullpath)




def nmap_log_to_csv(timestr, nmap_cmd_string, target, nmap_output_file):
    noping = 'False'
    verbose = 'False'
    os_detect = 'False'
    proxychain = 'False'
    traceroute = 'False'
    print colored('DEBUG LOG: noping = %s verbose = %s os_detect = %s proxychain = %s traceroute = %s','red',attrs=['bold']) % (
        noping,
        verbose,
        os_detect,
        proxychain,
        traceroute
    )

    # this should be immediately set to autorun after each nmap scan
    nmap_log_dir = '/root/ArmsCommander/logs/nmap/'
    # we dont need to open a file or read any line, its a variable passed from the nmap itself, into this function and module
    # determines if any of the five parameters set to default above, was acutally used
    # if used, it changes the value to TRUE (as a string)
    if re.findall('-v', nmap_cmd_string):
        verbose = 'True'
    if re.findall('-Pn', nmap_cmd_string):
        noping = 'True'
    if re.findall('-O', nmap_cmd_string):
        os_detect = 'True'
    if re.findall('sudo proxychains', nmap_cmd_string):
        proxychain = 'True'
    if re.findall('traceroute', nmap_cmd_string):
        traceroute = 'True'
    if re.findall('-sF', nmap_cmd_string):
        scan_type = 'FIN scan'
    if re.findall('-sX', nmap_cmd_string):
        scan_type = 'XMAS scan'
    if re.findall('-sS', nmap_cmd_string):
        scan_type = 'COMPREHENSIVE SYN SCAN'

    csv_file = nmap_log_dir + 'nmap_' + target + '_log.csv'
    # print colored('DEBUG LOG: csv_file set to %s','red',attrs=['bold']) % csv_file
    first_line = 'TIME SCANNED, TARGET, SCAN TYPE, NO PING?, VERBOSE?, DETECT OS?, PROXYCHAINED?, TRACEROUTE?, NMAP OUTPUT FILE\n'
    w = open(csv_file,'a+')
    # debug_text('DEBUG LOG: csv_file opened as APPEND/READ')
    # if re.findall("(?!^.*TIME SCANNED, TARGET, SCAN TYPE, NO PING?, VERBOSE?, DETECT OS?, PROXYCHAINED?, TRACEROUTE?, NMAP OUTPUT FILE*$).*", csv_file)): # use negative lookahead assertion
    # negative_regex_expression = '?!^.*' + string_var + '*$'
    negative_regex_expression = '^(?!.*' + first_line + ').*$'

    if re.findall(negative_regex_expression, csv_file): # regex cannot find the header line
        w.write(first_line) # write header line on top


        new_string = '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (timestr, target, scan_type, noping, verbose, os_detect, proxychain, traceroute, nmap_output_file)
        w.write(new_string)
        w.close()
        print colored('CSV LOGFILE SAVED, located at: %s','green',attrs=['bold']) % csv_file
        print colored('You can import this file into Excel, Google Sheets, LibreOffice Calc, whatever that processes .csv files','green',attrs=['bold'])
        return csv_file
    elif re.findall(first_line, csv_file): # regex has detected the header line
        new_string = '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (timestr, target, scan_type, noping, verbose, os_detect, proxychain, traceroute, nmap_output_file)
        w.write(new_string)
        w.close()
        print colored('CSV LOGFILE SAVED, located at: %s','green',attrs=['bold']) % csv_file
        print colored('You can import this file into Excel, Google Sheets, LibreOffice Calc, whatever that processes .csv files','green',attrs=['bold'])
    return csv_file

def credit_card_info_to_csv():
    return

def cornharvester_to_csv(cornharvester_output_file): # THis will integrate the abilities of SHODAN result splitter

    cornharvester_log_dir = '/root/ArmsCommander/logs/CornHarvester/'
    hosts_file = cornharvester_output_file + '_ips_and_hosts.csv'
    email_file = cornharvester_output_file + '_emails.csv'
    hosts_only_file = cornharvester_output_file + '_hosts_only.txt'

    r = open(cornharvester_output_file,'r')
    x = open(hosts_file,'a+')
    y = open(email_file,'a+')
    z = open(hosts_only_file,'a+')
    with open(cornharvester_output_file,'r') as r:
        line = r.readline()
        sentence = str(line) # you still have to format the line as a string apparently

        for sentence in r:
            if re.findall(':', str(sentence)): # why do I need to constantly format it as a string at every fucking line?
                # erases the contact information from TheHarvester
                sentence = sentence.replace('edge-security.com','')
                sentence = sentence.replace('[+] Emails found,\n','')
                sentence = sentence.replace('[+] Shodan Database search,\n','')
                sentence = sentence.replace('[+] Virtual hosts,\n','')
                sentence = sentence.replace('[+] Hosts found in search engines,\n','')
                sentence = sentence.replace('* cmartorella','')
                sentence = sentence.replace('* cmartorella@edge-security.com','')
                sentence = sentence.replace(r'^$','')
                sentence = sentence.split(':')
                ip_addr = sentence[0]
                host_name = sentence[1]
                write_string = '%s,%s' % (ip_addr, host_name)
                x.write(write_string)
                write_string = '%s' % host_name
                z.write(write_string)
                # print colored('DEBUG LOG: Wrote string: %s to HOSTS CSV file: %s','yellow',attrs=['bold']) % (write_string, hosts_file)

            if re.findall('@', str(sentence)):
                # print colored('DEBUG LOG: Valid Email Address detected, sentence: %s','green',attrs=['bold']) % sentence
                # erases the contact information from TheHarvester

                sentence = sentence.replace('edge-security.com','')
                sentence = sentence.replace('[+] Emails found,\n','')
                sentence = sentence.replace('[+] Shodan Database search,\n','')
                sentence = sentence.replace('[+] Virtual hosts,\n','')
                sentence = sentence.replace('[+] Hosts found in search engines,\n','')
                sentence = sentence.replace('* cmartorella','')
                sentence = sentence.replace('* cmartorella@edge-security.com','')
                sentence = sentence.replace(r'^$','')
                sentence = sentence.strip()
                full_email = sentence
                sentence = sentence.split('@')
                username = sentence[0]
                domain = sentence[1]
                write_string = '%s,%s' % (username, full_email)
                y.write(write_string)
                # print colored('DEBUG LOG: Wrote string: %s to EMAILS CSV file: %s','yellow',attrs=['bold']) % (write_string, email_file)
        x.close()
        y.close()
        z.close()
        print colored('Three files have been created','yellow',attrs=['bold'])
        print colored('DNS/HOSTS/IPs FILE: %s','green',attrs=['bold']) % hosts_file
        print colored('EMAILS FILE: %s','green',attrs=['bold']) % email_file
        print colored('HOSTS-ONLY FILE (to be fed back into CornHarvester): %s') % hosts_only_file

    return hosts_file, email_file, hosts_only_file



  # FTP, SSH, Telnet, HTTP(S), POP3(S), SMB, RDP, VNC, SIP, Redis, PostgreSQL, MySQL

# ftp = 21
# telnet = 23
# ssh  = 22
# http = 80
# https = 443
# pop3 = 110
# pop3s = 995
# smb 1 = 139
# smb 2 = 445
# rdp = 3389
# vnc = 5800
# sip = 5060 and 5061
# redis = 6379
# postgresql = 5432
# mysql = 3306

def nmap_read_wordlist(wordlist):
    r = open(wordlist, 'r')
    with open(wordlist, 'r') as r:
        line = r.readline().rstrip()
        line = line.replace('\n','')
        sentence = str(line)
        sentence = sentence.rstrip()
        sentence = sentence.replace('\n','')
        for sentence in r:
            nmap_dir = '/root/ArmsCommander/logs/nmap'
            ip_addr = sentence.replace('\n','')
            # port_range = '21-23, 80, 443, 110, 995, 139, 445, 3389, 5800, 5060, 5061, 6379, 5432, 3306'
            port_range = '1-6400'
            nmap_save_file = nmap_dir + '/mass_scan_savefile.txt'
            # nmap_save_file = nmap_save_file.replace('/','_')
            print colored('Running nmap scan against: %s on port ranges: %s','yellow',attrs=['bold']) % (ip_addr,port_range)
            cmd_String = "sudo proxychains nmap %s -p %s > %s" % (ip_addr, port_range, nmap_save_file)
            print colored(cmd_String,'red',attrs=['bold'])
            os.system(cmd_String)
            # read the save file
            r = open(nmap_save_file,'r')
            with open(nmap_save_file,'r') as r:
                print colored('Reading %s','yellow',attrs=['bold']) % nmap_save_file
                line = r.readline().rstrip()
                sentence = str(line)
                for sentence in r:
                    target_ip = ip_addr
                    if re.findall('open', str(sentence)): # discovered opened port
                        # print colored('Discovered open port','yellow',attrs=['bold'])
                        sentence = sentence.split()
                        target_port = sentence[0]
                        target_port = target_port.replace('/','_')
                        target_state = sentence[1]
                        target_service = sentence[2]

                        write_file_name = nmap_dir + '/' + target_port + '_open_' + target_service + '.csv'
                        # print colored('Vulnerable server detected, opening write file: %s','yellow',attrs=['bold']) % write_file_name
                        w = open(write_file_name, 'a+')
                        write_string = 'HOST:,%s,PORT:,%s,STATE:,%s,SERVICE:,%s\n' % (ip_addr, target_port, target_state, target_service)
                        w.write(write_string)
                        w.close()
                        print colored('Wrote HOST: %s PORT: %s STATE: %s SERVICE: %s as vulnerable to brute forcing in file: %s','green',attrs=['bold']) % (ip_addr, target_port, target_state, target_service, write_file_name)


    return nmap_save_file

def AWS_scanner():
    nmap_dir = '/root/ArmsCommander/logs/nmap'
    port_range = '1-6400'
    nmap_save_file = nmap_dir + '/AWS_scan_savefile.txt'
    ip_addr = '52.53.224.0/24'
    # nmap_save_file = nmap_save_file.replace('/','_')
    print colored('Running nmap scan against: %s on port ranges: %s','yellow',attrs=['bold']) % (ip_addr,port_range)
    cmd_String = "sudo proxychains nmap %s -p %s > %s" % (ip_addr, port_range, nmap_save_file)
    print colored(cmd_String,'red',attrs=['bold'])
    os.system(cmd_String)
    # read the save file
    r = open(nmap_save_file,'r')
    with open(nmap_save_file,'r') as r:
        print colored('Reading %s','yellow',attrs=['bold']) % nmap_save_file
        line = r.readline().rstrip()
        sentence = str(line)
        for sentence in r:
            target_ip = ip_addr
            if re.findall('open', str(sentence)): # discovered opened port
                # print colored('Discovered open port','yellow',attrs=['bold'])
                sentence = sentence.split()
                target_port = sentence[0]
                target_port = target_port.replace('/','_')
                target_state = sentence[1]
                target_service = sentence[2]

                write_file_name = nmap_dir + '/' + target_port + '_open_' + target_service + '.csv'
                # print colored('Vulnerable server detected, opening write file: %s','yellow',attrs=['bold']) % write_file_name
                w = open(write_file_name, 'a+')
                write_string = 'HOST:,%s,PORT:,%s,STATE:,%s,SERVICE:,%s\n' % (ip_addr, target_port, target_state, target_service)
                w.write(write_string)
                w.close()
                print colored('Wrote HOST: %s PORT: %s STATE: %s SERVICE: %s as vulnerable to brute forcing in file: %s','green',attrs=['bold']) % (ip_addr, target_port, target_state, target_service, write_file_name)


    return nmap_save_file
    # Typical syntax of ncrack
# ncrack -u test -P 500-worst-passwords.txt -T 5 10.10.10.10 -p 21

# ncrack commands has invalid charcter error not much help online so we are switching to hydra
def ncrack_ip_list(username_list, password_list, ip_list, port):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    cmd_String = "sudo proxychains ncrack -U %s -P %s -T 5 -iL %s -p %s -oN /root/ArmsCommander/logs/ncrack/%s.txt" % (username_list, password_list, ip_list, port, timestr)
    os.system(cmd_String)
    return

def hydra_ip_list(username_list, password_list, ip_list, protocol):
    cmd_String = "hydra -L %s -P %s -M %s %s" % (username_list, password_list, ip_list, protocol)
    print colored(cmd_String,'yellow',attrs=['bold'])
    os.system(cmd_String)
    return

def wordlist_cleaner(file_to_fix):
# note this toolkit is meant to correct the deficiencies of libreoffice. It was never meant to be used by the end user
    new_file = file_to_fix + '_fixed.txt'
    r = open(file_to_fix,'r+')
    with open(file_to_fix,'r+') as r:
        line = r.readline().strip()
        sentence = str(line)
        for sentence in r:
            sentence = sentence.replace('[+]','')
            sentence = sentence.replace('[','')
            sentence = sentence.replace(']','')
            sentence = sentence.replace('Shodan results','')
            sentence = sentence.replace('Emails found','')
            sentence = sentence.replace('Hosts found in search engines','')
            sentence = sentence.replace('results found','')
            sentence = sentence.replace('^$','')
            sentence = sentence.replace('Shodan Database search','')
            sentence = sentence.replace('Hosts found in search engines','')
            sentence = sentence.replace('Virtual hosts','')
            sentence = sentence.replace('cmartorella@edge-security.com','')
            sentence = sentence.replace('Virtual hosts','')
            sentence = sentence.replace('Shodan Database search','')
            w = open(new_file,'a+')
            w.write(sentence)
            print sentence
            w.close()
    print colored('Wordlist is now formatted into single line entries: %s','yellow',attrs=['bold']) % new_file

    return new_file


# typical hydra syntax
# hydra -L /root/Documents/basic_username_list -P /root/Documents/25-worst-passwords -M /rootocuments/ipwordlist.txt ssh
