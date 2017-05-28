import Missile_Lock_Toolkits
import os
import sys
import socket
import re
import time


def yellow(string):
    return

def red(string):
    return

def green(string):
    return

def monitor_mode():
    os.system('airmon-ng check kill')
    os.system('ifconfig wlan1 down')
    time.sleep(5)
    os.system('ifconfig wlan1 up')
    os.system('airmon-ng start wlan1')
    recon()
    return

def recon():
    Missile_Lock_Toolkits.save_recon_file()
    main()
    return

def targeted_and_replay():
    # Missile_Lock_Toolkits.read_temp_recon_file()
    # Missile_Lock_Toolkits.print_file_contents()
    Missile_Lock_Toolkits.open_attack_file()
    main()
    return

def resume_attack():

    return

def exit_to_cylon_raider():
    return

def main():
    opt_List = [
        '\n\t#0. Return to Cylon Raider Main Menu',
        '#1. MONITOR MODE',
        '#2. RECON',
        '#3. TARGETED SNIFFING & REPLAY-ATTACK',
        '#4. RESUME ATTACK'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        monitor_mode()
    elif opt_Choice == "2":
        recon()
    elif opt_Choice == "3":
        targeted_and_replay()
    elif opt_Choice == "4":
        resume_attack()
    elif opt_Choice == "0":
        exit_to_cylon_raider()
    else:
        main()
    return
main()
