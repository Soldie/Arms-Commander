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
from termcolor import colored
#import collections

# defining variables
BSSID_targeting_str = 'BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID'
CLIENT_targeting_str = 'BSSID              STATION            PWR   Rate    Lost    Frames  Probe'
successful_handshake_capture_str = 'WPA handshake:'
capture_Interface = 'wlan1mon'

# defining temporary files
temp_airodump_recon_capture_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_capture.cap'
temp_airodump_recon_csv_file = 'airodump_recon_file_csv_temp.csv'
temp_airodump_recon_file = 'airodump_recon_file_csv_temp.csv'
analysis_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv_temp.csv'
temp_file_airodump_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_airodump_targeted.csv'
temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_CLIENT_targeted.csv'

# defining devnull
DEVNULL = open(os.devnull, 'w')
# sys.stdout = DN

# it should be...
#         1. Recon file
#         2. Parsed into single line target number write_a_d_targeted_bssid files
#         3. Which can be called upon after being printed out again
        # 4. So there is really no "recon file". Its still being parsed into the targeted files
        # 5. instead we can start the airodump again as a subprocess and have the program check for us


# 1. User runs Airmon and Airodump as normal
# 2. Background, subprocess does tjhe same exact thing and records the information on the screen into a file
# 3. As soon as user stops the recon airodump, this toolkit begins the processing phase of the output
# 4. It will determine what part of the screen output is ACCESS POINT targeting. And the other part would be CLIENT mac address targeting
# 5. It auto-saves three temporary files in total, in csv format with the first value being the "target number"
# 6. After processing (it'll take just a split second) this toolkit will re-present the potential targets, and their relative values in being able to have their handshakes stolen (signal quality, clients connected)
# 7. Keys are bound to a numbered list. And it counts from the first BSSID target, to the last CLIENT target
# 8. At this point the three files are "tagged" with that they will do, with the file_type string so the program wont get confused
# 9. So one of the three files (third being the initial recon file) will attack WIRELESS APs, the other one will target connected CLIENTS that were observed on the NETWORK
# 10. All of these files are temporary, only when there is a verified handshake would there be a permanent file saved
# 11. for safe measure since handshakes can still get caught in recon mode, there will always be a condition where, if there is a handshake detected during recon mode, (someone just logged into network), the key is autosaved into a permanent file

target_number = 0

def read_temp_recon_file(temp_airodump_recon_file,target_number):

    # this is why stack overflow sucks, no real concrete answers
    r = open(temp_airodump_recon_file,'r')
    with open(temp_airodump_recon_file,'r') as r:
        try:
            line = r.readline().strip()
            for line in r:
                sentence = str(line)

                # print 'Current Target Number: %s For: %s' % (target_number, sentence)
                for sentence in r:

                    print 'Printing line in 3 seconds'
                    #time.sleep(3)
                    print line
                    print sentence
                    list = []
                    regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"
                    sentence = sentence.strip().split(',')
                    # print sentence
                    # target_list.append(sentence)
                    # target_number = target_list.index(sentence)
                    # print colored(target_number,'green',attrs=['bold'])
                    print 'Matching patterns in 3 seconds'
                    #time.sleep(3)
                    for sentence in r:
                        try:
                            if re.match(regex_mac_addr,sentence):
                                print colored(count_value,'yellow',attrs=['bold'])
                                print 'MAC ADDR FOUND'
                                print sentence
                                list = list.append['a']
                                target_number = list.count['a']
                                print sentence, target_number
                                sentence = sentence.split(',')
                                print sentence

                                print colored('DEBUG: reached function identify_and_assign_value_to_field_bssid_targeting(sentence,temp_file_BSSID_targeted, target_number)','red',attrs=['bold'])
                                print sentence
        try:
            string = 'DEBUG: contents of sentence file: %s' % sentence
            print colored(string,'yellow',attrs=['bold'])
            print sentence
            ESSID = sentence[13]
            BSSID = sentence[0]
            channel = sentence[3]
            signal_strength = sentence[8]
            encryption = sentence[5:7].join(',')
            print colored('TARGET NUMBER: %s \nESSID: %s \nBSSID: %s \nchannel: %s signal_strength: %s \n encryption: %s','red',attrs=['bold']) % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
            channel = sentence[3]
            signal_strength = sentence[8]
            encryption = sentence[5:7].join(',')
            print colored('DEBUG: Finished assigning variables','red',attrs=['bold'])
            print ESSID, BSSID, channel, signal_strength, encryption

            write_to_file(ESSID, BSSID, channel, signal_strength, encryption)

        except IndexError:
            print 'Found a CLIENT string: %s' % sentence
            pass
        return
                # except sentence[13] == ValueError:
                #     print 'Found a empty ESSID: %s' % sentence[13]
                #     if IndexError:
                #         pass
                #     pass

    sentence = sentence.split(',')
    print sentence

    print colored('DEBUG: reached function identify_and_assign_value_to_field_bssid_targeting(sentence,temp_file_BSSID_targeted, target_number)','red',attrs=['bold'])
    print sentence
    try:
        string = 'DEBUG: contents of sentence file: %s' % sentence
        print colored(string,'yellow',attrs=['bold'])
        print sentence
        ESSID = sentence[13]
        BSSID = sentence[0]
        channel = sentence[3]
        signal_strength = sentence[8]
        encryption = sentence[5:7].join(',')
        print colored('TARGET NUMBER: %s \nESSID: %s \nBSSID: %s \nchannel: %s signal_strength: %s \n encryption: %s','red',attrs=['bold']) % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
        channel = sentence[3]
        signal_strength = sentence[8]
        print colored('DEBUG: Finished assigning variables','red',attrs=['bold'])
        print ESSID, BSSID, channel, signal_strength, encryption

        write_to_file(ESSID, BSSID, channel, signal_strength, encryption)

    except IndexError:
        print 'Found a CLIENT string: %s' % sentence
        pass
        # except sentence[13] == ValueError:
        #     print 'Found a empty ESSID: %s' % sentence[13]
        #     if IndexError:
        #         pass
        #     pass
    except IOError:
        pass
