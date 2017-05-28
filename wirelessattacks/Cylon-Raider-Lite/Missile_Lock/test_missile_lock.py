import Missile_Lock_Toolkits
import Missile_Lock
import re
import os
import socket
import time

# defining variables
BSSID_targeting_str = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
CLIENT_targeting_str = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
successful_handshake_capture_str = 'WPA handshake:'
capture_Interface = 'wlan1mon'

# defining temporary files
permanent_file = '/root/Cylon-Raider-Lite/Missile_Lock/permanent_capture.cap'
name_for_output_airodump = '/root/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_'
recon_file = '/root/Cylon-Raider-Lite/Missile_Lock/airodump_recon_file_csv_temp.csv'
temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/Missile_Lock/temp_file_BSSID_targeted.csv'
temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/Missile_Lock/temp_file_CLIENT_targeted.csv'
regex_mac_addr = r"^((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}"
target_number = 0

def yellow(string):
    string = colored('%s','yellow',attrs=['bold']) % string
    return string

yellow('Beginning save-file-format test in three seconds')
time.sleep(3)
Missile_Lock_Toolkits.read_temp_recon_file(recon_file, regex_mac_addr)
yellow('Save-test complete, proceeding to print test in five seconds')
time.sleep(5)
cmd_String = 'cat %s' % temp_file_CLIENT_targeted
os.system(cmd_String)
cmd_String = 'cat %s' % temp_file_BSSID_targeted
os.system(cmd_String)
