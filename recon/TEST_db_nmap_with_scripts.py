import os
import sys
import operator
import socket
from termcolor import colored
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

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


os.chdir("/root/ArmsCommander/recon")

# Metasploit Manual Start up Commands
print red("Starting up Metasploit services")
os.system('service postgresql start')
os.system('msfdb init')
os.system('msfdb start')

print red("Starting up Tor Service")
os.system("gnome-terminal -e 'bash -c \"tor; exec bash\"'")
dict_generic_script_options = {
    1: 'auth',
    2: 'broadcast',
    3: 'brute',
    4: 'default',
    5: 'discovery',
    6: 'dos',
    7: 'exploit',
    8: 'external',
    9: 'fuzzer',
    10: 'intrusive',
    11: 'malware',
    12: 'safe',
    13: 'version',
    14: 'vuln',
    15: 'auth,brute,discovery,dos,exploit,external,fuzzer,intrusive,malware,version,vuln',
    16: 'auth,discovery,external,safe,version,vuln',
    17: 'ssl-enum-ciphers.nse',
    18: 'ssl-known-key.nse',
    19: 'sip-enum-users.nse',
    20: 'smb-enum-users.nse',
    21: 'dns-srv-enum.nse',
    22: 'http-wordpress-enum.nse',
    23: 'http-enum.nse',
    24: 'http-userdir-enum.nse',
    25: 'cics-enum.nse',
    26: 'cics-user-enum.nse',
    27: 'krb5-enum-users.nse',
    28: 'msrpc-enum.nse',
    29: 'mysql-enum.nse',
    30: 'rdp-enum-encryption.nse',
    31: 'smtp-enum-users.nse',
    32: 'ssh2-enum-algos.nse'
}

options_list = """
    For this question, type the corresponding number that represents the type of script you want to use.

    ### GENERIC USE-ALL SCRIPTS ###

    Note that this is a GENERIC USE-ALL scripts of the selected category.

    I do not recommend using #15 or #16 because it will attempt to run EVERYTHING, which takes days to complete for a single IP

    1: 'auth',
    2: 'broadcast',
    3: 'brute', Attempt to brute-force commonly and easily guessed credentials
    4: 'default',
    5: 'discovery', Find more information about the target, encryption method, etc.
    6: 'dos', Scan for Denial-Of-Service Vulnerabilities, may cause the target to crash
    7: 'exploit', Actively attempt to run exploits during the NMap scan
    8: 'external', Query third party sources online for enumeration
    9: 'fuzzer', Enter unexpected data during the scan to trigger errors and locate possible vulnerabilities
    10: 'intrusive',
    11: 'malware', Check if the target is infected with known malware
    12: 'safe',
    13: 'version',
    14: 'vuln', Check commonly known vulnerabilities
    15: AGGRESSIVE AND LOUD (and may crash a server) 'auth,brute,discovery,dos,exploit,external,fuzzer,intrusive,malware,version,vuln',
    16: DISCRETE AND STEALTHY 'auth,discovery,external,safe,version,vuln'

    ### CUSTOM FAVORITES ###

    17: 'ssl-enum-ciphers.nse',
    18: 'ssl-known-key.nse',
    19: 'sip-enum-users.nse',
    20: 'smb-enum-users.nse',
    21: 'dns-srv-enum.nse',
    22: 'http-wordpress-enum.nse',
    23: 'http-enum.nse',
    24: 'http-userdir-enum.nse',
    25: 'cics-enum.nse',
    26: 'cics-user-enum.nse',
    27: 'krb5-enum-users.nse',
    28: 'msrpc-enum.nse',
    29: 'mysql-enum.nse',
    30: 'rdp-enum-encryption.nse',
    31: 'smtp-enum-users.nse',
    32: 'ssh2-enum-algos.nse'
"""
tmp_resource_file = "./db_nmap_temp_file.rc"

def db_nmap():
    os.chdir("/root/ArmsCommander/recon")

    print options_list


    script_choice = int(raw_input(cyan("Enter a number to select the type of nmap scan you want to perform: ")))
    target_ip = str(raw_input(cyan("Enter either a IP address, range, or hostname to scan: ")))

    # FIN SCAN, gets past firewalls
    # print "Starting PASS ONE: A FIN Scan"
    print cyan("Starting PASS ONE: A FIN Scan")
    cmd_str = """db_nmap -v -O -sF -Pn -T4 -O -F --script={0} {1}
    exit""".format(
        dict_generic_script_options[script_choice],
        target_ip
    )

    print cmd_str
    w = open(tmp_resource_file,'w')
    w.write(cmd_str)
    w.close()

    debug_str = "cat {0}".format(cmd_str)
    os.system(debug_str)
    print "RESOURCE FILE CREATED: %s" % tmp_resource_file

    run_resource_file_str = "tsocks msfconsole -r ./db_nmap_temp_file.rc"

    print "RUNNING RESOURCE FILE: %s" % run_resource_file_str


    os.system(run_resource_file_str)

    # XMAS scan
    # print "Starting PASS TWO: A XMas Scan"
    print cyan("Starting PASS TWO: A XMas Scan")
    cmd_str = """db_nmap -v -O -sX -Pn -T4 -O -F --script={0} {1}
    exit""".format(
        dict_generic_script_options[script_choice],
        target_ip
    )

    w = open(tmp_resource_file,'w')
    w.write(cmd_str)
    w.close()

    debug_str = "cat {0}".format(cmd_str)
    os.system(debug_str)
    print "RESOURCE FILE CREATED: %s" % tmp_resource_file

    run_resource_file_str = "tsocks msfconsole -r ./db_nmap_temp_file.rc"

    print "RUNNING RESOURCE FILE: %s" % run_resource_file_str

    os.system(run_resource_file_str)

    #Comprehensive Scan
    # print "Starting PASS THREE: A COMPREHENSIVE Scan"
    print cyan("Starting PASS THREE: A COMPREHENSIVE Scan")
    cmd_str = """db_nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script={0} {1}
    exit""".format(
        dict_generic_script_options[script_choice],
        target_ip
    )

    w = open(tmp_resource_file,'w')
    w.write(cmd_str)
    w.close()

    debug_str = "cat {0}".format(cmd_str)
    os.system(debug_str)
    print "RESOURCE FILE CREATED: %s" % tmp_resource_file

    run_resource_file_str = "tsocks msfconsole -r ./db_nmap_temp_file.rc"

    print "RUNNING RESOURCE FILE: %s" % run_resource_file_str

    os.system(run_resource_file_str)
    return

def tsocks_nmap():
    os.chdir("/root/ArmsCommander/logs/nmap")
    print options_list


    script_choice = int(raw_input("Enter a number to select the type of nmap scan you want to perform: "))
    target_ip = str(raw_input("Enter either a IP address, range, or hostname to scan: "))
    savefile_name = str(raw_input("Enter a savefile name WITHOUT a file extension, example ('testname'): "))

    # FIN SCAN, gets past firewalls
    # print "Starting PASS ONE: A FIN Scan"
    print cyan("Starting PASS ONE: A FIN Scan")
    cmd_str = """tsocks nmap -v -O -sF -Pn -T4 -O -F -oA {0} --script={1} {2}
    exit""".format(
        savefile_name,
        dict_generic_script_options[script_choice],
        target_ip
    )
    os.system(cmd_str)
    # XMAS scan
    # print "Starting PASS TWO: A XMas Scan"
    print cyan("Starting PASS TWO: A XMas Scan")
    cmd_str = """tsocks nmap -v -O -sX -Pn -T4 -O -F -oA {0} --script={1} {2}
    exit""".format(
        savefile_name,
        dict_generic_script_options[script_choice],
        target_ip
    )
    os.system(cmd_str)

    #Comprehensive Scan
    # print "Starting PASS THREE: A COMPREHENSIVE Scan"
    print cyan("Starting PASS THREE: A COMPREHENSIVE Scan")
    cmd_str = """tsocks nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 -oA {0} --script={1} {2}
    exit""".format(
        savefile_name,
        dict_generic_script_options[script_choice],
        target_ip
    )
    os.system(cmd_str)

    complete_str = """NMAP scans complete, check your scans at: /root/ArmsCommander/logs/nmap/{0}
    """.format(
        savefile_name
    )
    print green(complete_str)
    return

def metasploit_nmap_question():
    intro_str = """
    Dear User,

    You have two options for the NMap scripting engine automater (name tentative to change)

    1. Run NMap through METASPLOIT FRAMEWORK -- Scans are automatically added to your MSF Hosts Database file
    2. Or run NMap INDEPENDENTLY -- Scans will generate three output results that are located in your /root/ArmsCommander/logs/nmap directory

    Both methods are properly anonymized via Tor and TSocks (which comes with your Arms-Commander Installation)

    Which method would you choose? Answer 'Y' to run this through Metasploit or 'N' to run it independently.
    """

    print yellow(intro_str)
    question = str(raw_input(cyan("Would you like to run the scan through Metasploit? (db_nmap, auto adds to your hosts file)? Y or N: ")))

    if question == "Y":
        db_nmap()
        main()
    elif question == "N":
        tsocks_nmap()
        main()
    else:
        print red("Please enter 'Y' or 'N'")
        metasploit_nmap_question()

    # if question == True:
    #     os.system('clear')
    #     db_nmap()
    #     main()
    # else:
    #     tsocks_nmap()
    #     main()
    return metasploit_nmap_question

def main():
    metasploit_nmap_question()
    main()
    return
main()
