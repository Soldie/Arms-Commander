  	#scan_Cmd_String = "proxychains nmap -v -O %s %s -f %s -S %s -e %s -T4 -F --version-light --traceroute --spoofmac %s -oN %s" %
#We have the following variables that can be set as a class attribute

    #(scan_Type,
    #scan_Ping_Yes_No,
    #scan_Fragment_Amt,
    #scan_Spoof_IP,
    #scan_Interface,
    #scan_Spoof_MAC,
    #scan_Target,
    #scan_Output_Location)

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

# all Dict files go here:

        #    SCAN TECHNIQUES:
        #      -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
        #      -sU: UDP Scan
        #      -sN/sF/sX: TCP Null, FIN, and Xmas scans
        #      --scanflags <flags>: Customize TCP scan flags
        #      -sI <zombie host[:probeport]>: Idle scan
        #      -sY/sZ: SCTP INIT/COOKIE-ECHO scans
        #      -sO: IP protocol scan
        #      -b <FTP relay host>: FTP bounce scan

scan_Dict = {
    'SYN': '-sS',
    'Connect': '-sT',
    'ACK': '-sA',
    'Window': '-sW',
    'Maimon': '-sM',
    'UDP': '-sU',
    'Null': '-sN',
    'FIN': '-sF',
    'Xmas': '-sX',
    'Idle': '-sI',
    'Zombie': '-sI',
    'SCTP INIT': '-sY',
    'COOKIE-ECHO': '-sZ',
    'IP Protocol': '-sO',
    'FTP Bounce': '-b'
}

os.system('cat /root/ArmsCommander/banners/CustomNmapScanList.txt')

scan_question = colored('SCAN TYPE (Enter from the list): ','yellow',attrs=['bold'])
ping_question = colored('PING SCAN? Type -Pn=No Ping or Leave BLANK: ','yellow',attrs=['bold'])
timing_question = colored('TIMING MODE (0=SNEAKY, 5=AGGRESSIVE): ','yellow',attrs=['bold'])
os_question = colored('OS DETECTION INTENSITY (0=LIGHT, 9=INTENSE): ','yellow',attrs=['bold'])
target_question = colored('TARGET IP: ','yellow',attrs=['bold'])
output_question = colored('OUTPUT FILE, FULL DIRECTORY: ','yellow',attrs=['bold'])
#Create a overview of the class and what datafields are there
class ScanParameters(object):
    #define a template for the class basically, te fields will alwyas fill in this order from the initialize function
    def __init__ (self, scantype, ping, TimingMode, Intensity, target_IP, output_File): #the problem is that it is stored in EXACLTLY this order in syntax
        self.scantype = scantype # Apparently it is NOT easily done to have a dictionary associated with a class
        self.ping = ping
        self.TimingMode = TimingMode
        self.Intensity = Intensity
        self.target_IP = target_IP
        self.output_File = output_File

# for some reason I completely lost my NMap Custom Code I will need to rebuild the dicts
    #define the user input part of the class for each field
    #this is your chance to make it "user-friendly"
    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input(scan_question)),
            str(raw_input(ping_question)),
            str(raw_input(timing_question)),
            str(raw_input(os_question)),
            str(raw_input(target_question)),
            str(raw_input(output_question))
        )

#Mandatory to be able to call the values back
CustomScan = ScanParameters.from_input()
#To call upon a value entered by user it is CustomScan.AttributeField

print colored('Now running command with the following parameters','green',attrs=['bold'])

print colored('SCAN TYPE: ' + scan_Dict[CustomScan.scantype],'red',attrs=['bold'])
print colored('PING SETTING: ' + CustomScan.ping,'red',attrs=['bold'])
print colored('TIMING MODE: ' + CustomScan.TimingMode,'red',attrs=['bold'])
print colored('INTENSITY: ' + CustomScan.Intensity,'red',attrs=['bold'])
print colored('TARGET: ' + CustomScan.target_IP,'red',attrs=['bold'])
print colored('OUTPUT FILE: ' + CustomScan.output_File,'red',attrs=['bold'])
time.sleep(1)

scan_Cmd_String = "proxychains nmap -v -O %s %s -T%s --version-intensity %s --traceroute %s -oN %s" % (
                                                                                                                                scan_Dict[CustomScan.scantype],
                                                                                                                                CustomScan.ping,
                                                                                                                                CustomScan.TimingMode,
                                                                                                                                CustomScan.Intensity,
                                                                                                                                CustomScan.target_IP,
                                                                                                                                CustomScan.output_File)
# print colored(scan_Cmd_String,'red',attrs=['bold'])

os.system(scan_Cmd_String)

print colored('[+] Scan complete, please check %s for your results','green',attrs=['bold']) % CustomScan.output_File
