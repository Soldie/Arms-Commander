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
            str(raw_input('SCAN TYPE (Enter from the list): ')),
            str(raw_input('PING SCAN? Type -Pn=No Ping or Leave BLANK: ')),
            str(raw_input('TIMING MODE (0=SNEAKY, 5=AGGRESSIVE): ')),
            str(raw_input('OS DETECTION INTENSITY (0=LIGHT, 9=INTENSE): ')),
            str(raw_input('TARGET IP: ')),
            str(raw_input('OUTPUT FILE, FULL DIRECTORY: '))
        )

#Mandatory to be able to call the values back
CustomScan = ScanParameters.from_input()
#To call upon a value entered by user it is CustomScan.AttributeField


scan_Cmd_String = "proxychains nmap -v -O %s %s -T%s --version-intensity %s --traceroute %s -oN %s" % (
                                                                                                                                scan_Dict[CustomScan.scantype],
                                                                                                                                CustomScan.ping,
                                                                                                                                CustomScan.TimingMode,
                                                                                                                                CustomScan.Intensity,
                                                                                                                                CustomScan.target_IP,
                                                                                                                                CustomScan.output_File)
print colored(scan_Cmd_String,'red','on_white')
os.system(scan_Cmd_String)
