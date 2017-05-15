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

def shodan_result_splitter(input_file, query):
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
        # nmap_cmd_string = "sudo proxychains nmap -v -O -sF -Pn -T4 -O -F --version-light --traceroute %s -oN %s" % (scan_Target, nmap_logfile_fullpath)




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
    if re.findall('proxychains', nmap_cmd_string):
        proxychain = 'True'
    if re.findall('traceroute', nmap_cmd_string):
        traceroute = 'True'
    if re.findall('-sF', nmap_cmd_string):
        scan_type = 'FIN scan'
    if re.findall('-sX', nmap_cmd_string):
        scan_type = 'XMAS scan'
    if re.findall('-sS', nmap_cmd_string):
        scan_type = 'COMPREHENSIVE SYN SCAN'
    # print colored('DEBUG LOG, scanned command string, variable changed: noping = %s verbose = %s os_detect = %s proxychain = %s traceroute = %s','red',attrs=['bold']) % (
    #     noping,
    #     verbose,
    #     os_detect,
    #     proxychain,
    #     traceroute
    # )
    # print colored('DEBUG LOG, import parameter test: time = %s target = %s scan_type = %s nmap_output_file = %s','red',attrs=['bold']) % (
    #     timestr,
    #     target,
    #     scan_type,
    #     nmap_output_file
    # )
    csv_file = nmap_log_dir + 'nmap_' + target + '_log.csv'
    # print colored('DEBUG LOG: csv_file set to %s','red',attrs=['bold']) % csv_file
    first_line = '\nTIME SCANNED, TARGET, SCAN TYPE, NO PING?, VERBOSE?, DETECT OS?, PROXYCHAINED?, TRACEROUTE?, NMAP OUTPUT FILE'
    w = open(csv_file,'a+')
    # debug_text('DEBUG LOG: csv_file opened as APPEND/READ')
    # if re.findall("(?!^.*TIME SCANNED, TARGET, SCAN TYPE, NO PING?, VERBOSE?, DETECT OS?, PROXYCHAINED?, TRACEROUTE?, NMAP OUTPUT FILE*$).*", csv_file)): # use negative lookahead assertion
    # negative_regex_expression = '?!^.*' + string_var + '*$'
    negative_regex_expression = '^(?!.*' + first_line + ').*$'

    if re.findall(negative_regex_expression, csv_file): # regex cannot find the header line
    # writes the first-line heading row to be used in spreadsheets like Excel to create "columns"
        w.write(first_line) # write header line on top
        # print colored('DEBUG LOG: Cannot find first_line variable, writing new header line','yellow',attrs=['bold'])
        # print colored('DEBUG LOG: First line written as "%s"','red',attrs=['bold']) % first_line

        new_string = '\n%s,%s,%s,%s,%s,%s,%s,%s,%s' % (timestr, target, scan_type, noping, verbose, os_detect, proxychain, traceroute, nmap_output_file)
        w.write(new_string)
        w.close()
        print colored('CSV LOGFILE SAVED, located at: %s','green',attrs=['bold']) % csv_file
        print colored('You can import this file into Excel, Google Sheets, LibreOffice Calc, whatever that processes .csv files','green',attrs=['bold'])
        return csv_file
    # print colored('DEBUG LOG: First line written as "%s"','red',attrs=['bold']) % first_line
    elif re.findall(first_line, csv_file): # regex has detected the header line
        # print colored('DEBUG LOG: Regex has detected a header line, writing a new log string instead','yellow',attrs=['bold'])
        new_string = '\n%s,%s,%s,%s,%s,%s,%s,%s,%s' % (timestr, target, scan_type, noping, verbose, os_detect, proxychain, traceroute, nmap_output_file)
        w.write(new_string)
        w.close()
        print colored('CSV LOGFILE SAVED, located at: %s','green',attrs=['bold']) % csv_file
        print colored('You can import this file into Excel, Google Sheets, LibreOffice Calc, whatever that processes .csv files','green',attrs=['bold'])
    return csv_file

def credit_card_info_to_csv():
    return

def cornharvester_to_csv(cornharvester_output_file): # THis will integrate the abilities of SHODAN result splitter

    # print colored('DEBUG LOG: cornharvester output file = %s','red',attrs=['bold']) % cornharvester_output_file
    cornharvester_log_dir = '/root/ArmsCommander/logs/CornHarvester/'
    hosts_file = cornharvester_output_file + '_hosts.csv'
    # print colored('DEBUG LOG: hosts file = %s','red',attrs=['bold']) % hosts_file
    email_file = cornharvester_output_file + '_emails.csv'
    # print colored('DEBUG LOG: emails file = %s','red',attrs=['bold']) % email_file
    # ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
    #
    # Valid_Email_Regex = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63}$"
    #
    # # ValidIpAddressRegex = "^\d\.\d\.\d.\d$"
    # ValidIpAddressRegex = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    # read the lines of the file
    r = open(cornharvester_output_file,'r')
    x = open(hosts_file,'a+')
    y = open(email_file,'a+')
    with open(cornharvester_output_file,'r') as r:
        line = r.readline()
        sentence = str(line) # you still have to format the line as a string apparently
        # print colored('DEBUG LOG: Successfully read the line into a buffer','red',attrs=['bold'])
        for sentence in r:
            if re.findall(':', str(sentence)): # why do I need to constantly format it as a string at every fucking line?
                # print colored('DEBUG LOG: Valid IP detected, LINE: %s','green',attrs=['bold']) % sentence
                # organize it into a CSV file and save it as a
                sentence = sentence.split(':')
                ip_addr = sentence[0]
                host_name = sentence[1]
                write_string = '\n%s,%s' % (ip_addr, host_name)
                x.write(write_string)
                # print colored('DEBUG LOG: Wrote string: %s to HOSTS CSV file: %s','yellow',attrs=['bold']) % (write_string, hosts_file)

            if re.findall('@', str(sentence)):
                # print colored('DEBUG LOG: Valid Email Address detected, sentence: %s','green',attrs=['bold']) % sentence
                full_email = sentence
                sentence = sentence.split('@')
                username = sentence[0]
                domain = sentence[1]
                write_string = '\n%s,%s,%s' % (domain, username, full_email)
                y.write(write_string)
                # print colored('DEBUG LOG: Wrote string: %s to EMAILS CSV file: %s','yellow',attrs=['bold']) % (write_string, email_file)
        x.close()
        y.close()
        print colored('Two files have been created','yellow',attrs=['bold'])
        print colored('DNS/HOSTS/IPs FILE: %s','green',attrs=['bold']) % hosts_file
        print colored('EMAILS FILE: %s','green',attrs=['bold']) % email_file
        # # if IP and/or hostname
        # if re.findall(ValidHostnameRegex, line):
        #     y = open(hosts_file,'a+')
        #     # organize it by IP, and then hostname into a CSV file
        # if email address

    return hosts_file, email_file



# import socket
#
# try:
#     socket.inet_aton(addr)
#     print "ipv4 address"
# except socket.error:
#     print "not ipv4 address"
#
# For IPv6 addresses you must use socket.inet_pton(socket.AF_INET6, address).
