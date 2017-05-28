#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import sys
import StringIO
import socket
import time

# out of mana is the Mana toolkit automater with new improved features including automatic packet capture

def start_mana():

    # Start mana toolkit
    os.system('airmon-ng stop wlan1mon')
    os.system('airmon-ng check kill') # kills all instances of monitor mode to let Mana work
    os.system('chmod 777 /usr/share/mana-toolkit/run-mana') # chmods the mana toolkit scripts if it hasn't been done already already
    # os.system('/usr/share/mana-toolkit/run-mana/start-nat-full.sh') # Runs the main script
    # # start TCP dump
    #
    # timestr = time.strftime("%Y%m%d-%H%M%S") # generates a unique filename by time
    # tcpdump_file_dir = '/root/Cylon-Raider-Lite/logs/mana_toolkit'
    # tcpdump_file_name = "%s/mana_toolkit_tcp_dump_%s.pcap" % (tcpdump_file_dir, timestr)
    #
    # # cmd_String = "tcpdump -i wlan1 -w %s" % tcpdump_file_name # runs TCP dump on interface wlan1 and writing to a tcpdumpfile at the specified location    # os.system(cmd_String)
    # # os.system("gnome-terminal -e 'bash -c \"%s; exec bash\"'") % cmd_String
    # cmd_String = "gnome-terminal -e 'bash -c \"tcpdump -i wlan1 -w %s.pcap; exec bash\"'" % tcpdump_file_name
    # # os.system("gnome-terminal -e 'bash -c \"tcpdump -i wlan1 -w {0}.pcap; exec bash\"'").format(
    # #     str(tcpdump_file_name)
    # )
    os.system('/usr/share/mana-toolkit/run-mana/start-nat-full.sh') # Runs the main script
    # time.sleep(5)
    # os.system(cmd_String)

def tcp_dump():
    timestr = time.strftime("%Y%m%d-%H%M%S") # generates a unique filename by time
    tcpdump_file_dir = '/root/Cylon-Raider-Lite/logs/mana_toolkit'
    tcpdump_file_name = "%s/mana_toolkit_tcp_dump_%s.pcap" % (tcpdump_file_dir, timestr)

    # cmd_String = "tcpdump -i wlan1 -w %s" % tcpdump_file_name # runs TCP dump on interface wlan1 and writing to a tcpdumpfile at the specified location    # os.system(cmd_String)
    # os.system("gnome-terminal -e 'bash -c \"%s; exec bash\"'") % cmd_String
    # cmd_String = "gnome-terminal -e 'bash -c \"tcpdump -i wlan1 -w %s.pcap; exec bash\"'" % tcpdump_file_name
    cmd_String = "tcpdump -i wlan1 -w %s" % tcpdump_file_name
    # os.system("gnome-terminal -e 'bash -c \"tcpdump -i wlan1 -w {0}.pcap; exec bash\"'").format(
    #     str(tcpdump_file_name)
    # )
    # os.system('/usr/share/mana-toolkit/run-mana/start-nat-full.sh') # Runs the main script
    # time.sleep(5)
    os.system(cmd_String)
    return

def configure_mana():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Edit /usr/share/mana-toolkit/run-mana/start-nat-full.sh',
        '#2. Edit /etc/mana-toolkit/dnsmasq-dhcpd.conf',
        '#3. Edit /etc/mana-toolkit/dnsspoof.conf',
        '#4. Edit /etc/mana-toolkit/hostapd-mana.conf'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('nano /usr/share/mana-toolkit/run-mana/start-nat-full.sh')
        configure_mana()
    elif opt_Choice == "2":
        os.system('nano /etc/mana-toolkit/dnsmasq-dhcpd.conf')
        configure_mana()
    elif opt_Choice == "3":
        os.system('nano /etc/mana-toolkit/dnsspoof.conf')
        configure_mana()
    elif opt_Choice == "4":
        os.system('nano /etc/mana-toolkit/hostapd-mana.conf')
        configure_mana()
    else:
        print 'You have entered a invalid option'
        configure_mana()
    return
def monitor_mode():
    os.system('ifconfig wlan1 up')
    os.system('airmon-ng start wlan1')
    os.system('airodump-ng wlan1mon')
    return
def main():
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#CONFIGURE. Configure Mana Toolkit Settings',
        '#1. START Mana-Toolkit',
        '#2. MONITOR MODE, run your external Wi-Fi Card in Monitor Mode to look for targets to spoof',
        '#3. TCP DUMP, generate a packet capture as you are running Mana. must be done after starting the Mana toolkit'
    ]

    print("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        start_mana()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        tcp_dump()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        monitor_mode()
        main()
    elif opt_Choice == "CONFIGURE" or "config" or "configure":
        os.system('clear')
        configure_mana()
        main()
    else:
        print 'You have entered a invalid option'
        main()

main()
