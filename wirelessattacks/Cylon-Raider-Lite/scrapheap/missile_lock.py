import os
from os import devnull
import socket
import sys
from multiprocessing import process
import subprocess
from subprocess import Popen, call, PIPE
import re
import time
from sys import argv
from sys import stdout
import Cylon_Toolkit
from Cylon_Toolkit import temp_file_CLIENT_targeted, temp_file_BSSID_targeted


# defining variables
BSSID_targeting_str = 'BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID'
CLIENT_targeting_str = 'BSSID              STATION            PWR   Rate    Lost    Frames  Probe'
successful_handshake_capture_str = 'WPA handshake:'
capture_Interface = 'wlan1mon'

# defining temporary files
temp_airodump_recon_capture_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_capture.cap'
temp_airodump_recon_csv_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv'
temp_file_airodump_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_airodump_targeted.csv'
temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_CLIENT_targeted.csv'

# defining devnull
DEVNULL = open(os.devnull, 'w')
# sys.stdout = DN
# class Logger(object):
#     def __init__(self):
#         self.terminal = stderr
#         self.log = open("/root/Cylon-Raider-Lite/logs/airodump_recon_file.log", "a")
#
#     def write(self,message):
#         self.terminal.write(message)
#         self.log.write(message)
#
#     def flush(self):
#         pass

def targeted_replay():
    os.system('clear')
    Cylon_Toolkit.display_targets(temp_file_CLIENT_targeted, temp_file_BSSID_targeted)
    return temp_file_CLIENT_targeted, temp_file_BSSID_targeted


def main():
    opt_List = [
        '\n\t#0. Return to Cylon Raider Main Menu',
        '#1. MONITOR MODE',
        '#2. RECON',
        '#3. TARGETED SNIFFING & REPLAY ATTACK',
        '#4. RESUME REPLAY ATTACK, in case you screwed it up seconds later (OTG wire fell out of tablet or something)'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "0":
        os.system('python /root/Cylon-Raider-Lite/Cylon_Raider_Main.py')
    elif opt_Choice == "1":
        os.system('clear')
        os.system('airmon-ng check kill')
        os.system('airmon-ng start wlan1')
        main()
    elif opt_Choice == "2":
        print 'Note, you need to cancel out of RECON mode (CTRL + C) to start the temporary save-state process that will let you do step 3'
        time.sleep(2)
        print 'The airodump-ng feed will be updated in 5 second intervals to a *.csv file'
        time.sleep(3)
        os.system('clear')
        cmd_String = "airodump-ng -i wlan1mon -w %s --write-interval 5 -o csv" % temp_airodump_recon_csv_file
        os.system(cmd_String)

        if re.match(successful_handshake_capture_str, temp_airodump_recon_csv_file):
            sentence = temp_airodump_recon_csv_file.split('WPA Handshake:')
            unexpected_BSSID = sentence[1]
            permanent_capture_file = unexpected_BSSID + '_permanent_capture_handshake_unexpected.cap'
            print 'ALERT: A handshake was detected whether or not you intended to capture it'
            print 'It is autosaved as %s' % permanent_capture_file
            os.system('cp -r %s %s') % (temp_airodump_recon_capture_file, permanent_capture_file)

        if KeyboardInterrupt:
            main()
        airodump_csv_output = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv*.csv'
        analysis_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv_temp.csv'
        cmd_String = 'cat %s > %s' % (airodump_csv_output, analysis_file)
        print analysis_file
        cmd_String = 'cat %s' % analysis_file
        os.system(cmd_String)
        print cmd_String
        temp_file_BSSID_targeted = Cylon_Toolkit.determine_type_of_file(analysis_file)
        temp_file_CLIENT_targeted = Cylon_Toolkit.determine_type_of_file(analysis_file)
        print temp_file_CLIENT_targeted, print temp_file_BSSID_targeted
        print 'Temporary recon file saved as: %s' % permanent_capture_file
        print 'Sending it in for parsing in the engine'

        return temp_airodump_recon_file, temp_airodump_recon_csv_file, permanent_capture_file, temp_file_BSSID_targeted, temp_file_CLIENT_targeted

    elif opt_Choice == "3":
        os.system('clear')
        targeted_replay()
    elif opt_Choice == "4":
        determine_targeted_capture(file_type)
        main()
    return temp_file_CLIENT_targeted, temp_file_BSSID_targeted

main()
