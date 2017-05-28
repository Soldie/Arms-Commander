import os
import socket
import re
import sys
from termcolor import colored
import StringIO

global hosts_file, hostname
global rw_rc_file, test_file_read, test_file_write, test_file_load
hosts_file = './hosts_file_smtp_scan.csv' # like hosts only files that I was making
rw_rc_file = './msf_rc_file_rwx.rc'

test_file_read = './test_file_hosts.csv'
test_file_write = './test_file_rwx.rc'

regex_IP_address = r"^\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

def yellow(string):
    string = colored('%s','yellow',attrs=['bold']) % string
    print string
    return string

def red(string):
    string = colored('%s','red',attrs=['bold']) % string
    print string
    return string
def green(string):
    string = colored('%s','green',attrs=['bold']) % string
    print string
    return string
def read_hosts_file(hosts_file):

    r = open(hosts_file,'r')
    read_r = r.read()
    buf = StringIO.StringIO(read_r)

    while True:
        try:
            line = buf.readline().strip()
            if line != "":
                # if re.match(regex_IP_address, line):
                #     line = line.split(regex_IP_address)
                #     hostname = str(line[0])
                #     generate_rc_file_and_execute(hostname)
                #     hostname = str(line[1])
                #     generate_rc_file_and_execute(hostname)
                hostname = str(line)
                generate_rc_file_and_execute(hostname, rw_rc_file)
            else:
                red('Reached EOF, closing program')
                exit(0)


        except IOError:
            pass


    return hostname

def generate_rc_file_and_execute(hostname, rw_rc_file):


    RPORT_LIST = [
        '25',
        '26',
        '587',
        '465'
    ]

    for RPORT in RPORT_LIST:

        w = open(rw_rc_file,'w')
        write_string = 'use auxiliary/scanner/smtp/smtp_relay\n'
        w.write(write_string)
        write_string = 'set RHOSTS %s\n' % hostname
        w.write(write_string)
        write_string = 'set RPORT %s\n' % RPORT
        w.write(write_string)
        write_string = 'set EXTENDED true\n'
        w.write(write_string)

        write_string = 'set THREADS 254\n'
        w.write(write_string)

        write_string = 'run\n'
        w.write(write_string)
        write_string = 'exit\n' # Allows you to exit msfconsole and then it'll execute the next script process
        w.write(write_string)
        w.close()



    #Open and write to rc file
    #Execution
        os.system('service postgresql start')
        os.system('service metasploit start')
        os.system('msfdb init')
        os.system('msfdb start')
        cmd_string = "msfconsole -r %s" % rw_rc_file
        os.system(cmd_string)

    return rw_rc_file

def convert_to_host_file(hosts_file):
    term_to_match = '/root/ArmsCommander/logs/CornHarvester/*hosts_only*'

    cmd_string = "cat %s > %s" % (term_to_match, hosts_file)
    os.system(cmd_string)
    green('Hosts file: %s') % hosts_file
    main()
    return hosts_file

def tester(test_file_read, test_file_write):
    yellow('Performing Read test file test')
    hostname = read_hosts_file(test_file_read)
    yellow('Performing write to test file test')
    generate_rc_file_and_execute(hostname, test_file_write)
    yellow('Performing the Start test file test')
    green('All tests complete')

    return
def main():
    print """
    \t\t\tCOMMANDS for SMTP mass-scanner\n
    \tSTART = start the cycle and autoscanning
    \tSET = change the location of your hostname files and rewritable *.rc file
    \tCONVERT = change a set of hostname files into a single wordlist of domains
    \tTEST = run the tester module, testing reading, writing, loading the rc files
    """
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "START":
        read_hosts_file(hosts_file)
    elif opt_Choice == "SET":
        return
    elif opt_Choice == "CONVERT":
        convert_to_host_file(hosts_file)
    elif opt_Choice == "TEST":
        tester(test_file_read, test_file_write)
    else:
        red('You have entered a invalid option')
        main()
    return
main()
