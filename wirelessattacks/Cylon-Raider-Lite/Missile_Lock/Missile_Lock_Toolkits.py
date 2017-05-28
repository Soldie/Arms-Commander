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

# defining variables
BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
successful_handshake_capture_str = 'WPA handshake:'
capture_Interface = 'wlan1mon'

# defining temporary files
permanent_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
name_for_output_airodump = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
recon_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
temp_file_BSSID_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
temp_file_CLIENT_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"
global target_number
target_number = 0

def open_attack_file():
    # defining variables
    BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
    CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
    successful_handshake_capture_str = 'WPA handshake:'
    capture_Interface = 'wlan1mon'

    # defining temporary files
    permanent_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
    name_for_output_airodump = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
    recon_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
    temp_file_BSSID_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
    regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"


    read_bssid_attack = open(temp_file_BSSID_targeted,'r')
    read_client_attack = open(temp_file_CLIENT_targeted,'r')

    read_bssid_attack = read_bssid_attack.readlines().strip()
    print read_bssid_attack
    read_client_attack = read_client_attack.readlines().strip()
    print read_client_attack

def variable_counter(sentence, regex_mac_addr):
    list = []
    for sentence in r:
        if re.match(regex_mac_addr,sentence):
            list = list.append('a')
            target_number = list.count('a')
            string = 'TARGET NUMBER: %s \nSTRING:' % (target_number, sentence)
            print colored(string,'yellow',attrs=['bold'])
        else:
            pass
    return target_number

def save_recon_file():
    cmd_String = "airodump-ng -w %s --write-interval 5 -o csv wlan1mon" % name_for_output_airodump

    os.system(cmd_String)
    cmd_String = "cat *%s* > %s" % (name_for_output_airodump, recon_file)
    os.system(cmd_String)
    read_temp_recon_file()
    return recon_file

def read_temp_recon_file():
    # defining variables
    BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
    CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
    successful_handshake_capture_str = 'WPA handshake:'
    capture_Interface = 'wlan1mon'

    # defining temporary files
    permanent_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
    name_for_output_airodump = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
    recon_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
    temp_file_BSSID_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
    regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"

    r = (open(recon_file,'r'))
    with open(recon_file,'r') as r:
        line = r.readline().strip()
        whole_file = r.readlines().strip()
        # paragraph_s = whole_file.split(BSSID_targeting_str)
        # paragraph_s = whole_file.split(CLIENT_targeting_str)
        # BSSID_paragraph = paragraph_s[-2]
        # CLIENT_paragraph = paragraph_s[-1]
        # print BSSID_paragraph
        # print CLIENT_paragraph
        for line in r:
            sentence = str(line)
            for sentence in r:
                sentence = str(sentence.split(','))

                try:
                    if re.match(regex_mac_addr, sentence):
                        target_number = variable_counter(target_number, sentence, regex_mac_addr)
                        make_BSSID_file(target_number, sentence, temp_file_BSSID_targeted)
                #except sentence[7] == IndexError: # whatever is in the seventh field for the client attack menu, we know its shorter
                except len(sentence) > 6:
                # find a unique key in that table
                    if re.match(regex_mac_addr, sentence): # change out regex_mac_addr
                        target_number = variable_counter(target_number, sentence, regex_mac_addr)
                        make_CLIENT_file(target_number, sentence, temp_file_CLIENT_targeted)
                    else:
                        pass
    return sentence, recon_file, regex_mac_addr

def make_BSSID_file(target_number, sentence, temp_file_BSSID_targeted):
    # defining variables
    BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
    CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
    successful_handshake_capture_str = 'WPA handshake:'
    capture_Interface = 'wlan1mon'

    # defining temporary files
    permanent_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
    name_for_output_airodump = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
    recon_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
    temp_file_BSSID_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
    regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"
    # check make sure snetence is still as a list
    print sentence
    ESSID = sentence[13]
    BSSID = sentence[0]
    channel = sentence[3]
    signal_strength = sentence[8]
    encryption = sentence[5:7].join(',')
    print colored('TARGET NUMBER: %s \nESSID: %s \nBSSID: %s \nchannel: %s signal_strength: %s \nencryption: %s','red',attrs=['bold']) % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
    write_string = '%s,%s,%s,%s,%s,%s,%s\n' % (target_number, ESSID, BSSID, channel, signal_strength, encryption)
    print 'Writing... %s to file: %s' % (sentence,temp_file_BSSID_targeted)
    print colored(write_string,'yellow',attrs=['bold'])
    #     #time.sleep(3)
    w = open(temp_file_BSSID_targeted,'w+')
    with open(temp_file_BSSID_targeted,'w+') as w:
        w.write(write_string)
        w.close()


    return temp_file_BSSID_targeted, write_string
def print_file_contents(temp_file_BSSID_targeted, temp_file_CLIENT_targeted):
    string = "cat %s" % temp_file_BSSID_targeted
    os.system(string)
    string = 'cat %s' % temp_file_CLIENT_targeted
    os.system(string)
    return
def make_CLIENT_file(target_number, sentence, temp_file_CLIENT_targeted):
    # defining variables
    BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
    CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
    successful_handshake_capture_str = 'WPA handshake:'
    capture_Interface = 'wlan1mon'

    # defining temporary files
    permanent_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
    name_for_output_airodump = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
    recon_file = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
    temp_file_BSSID_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
    regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"

    print sentence
    sentence = sentence.split(',')
    sentence = sentence.strip()
    CLIENT_MAC = sentence[0]
    signal_strength = sentence[3]
    connected_AP = sentence[5]
    probed_APs = sentence[6]
    print colored('TARGET NUMBER: %s Client Connected Wireless AP: %s Client MAC Addr: %s Signal: %s Other APs probed by Client: %s','yellow',attrs=['bold']) % (
        target_number,
        connected_AP,
        CLIENT_MAC,
        signal_strength,
        probed_APs
    )
    w = open(temp_file_CLIENT_targeted,'w')
    with open(temp_file_CLIENT_targeted,'w+') as w:
        w.write(write_string)
        w.close()

    return
