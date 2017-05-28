#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
# #from termcolor import colored
import sys
import time
from subprocess import *
from subprocess import Popen
from subprocess import PIPE
import threading

cap_file_dir = '/root/Cylon-Raider-Lite/logs'
capture_Interface = 'wlan1mon'
dev_null = open(os.devnull,'w')
# os.system('cat /root/Cylon-Raider-Lite/banner_airmon.txt')

# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# capture_Interface = str(raw_input("Enter the capture INTERFACE that was revealed to you in AIRMON: "))
# capture_Interface = CrackHead.airodump_String #For some reason this isnt working, it was supposed to import airodump_String from the first module
timestr = time.strftime("%Y%m%d-%H%M%S")
proc_String = "python /root/Cylon-Raider-Lite/sniffHidden.py"

def thread_1():
    # import variables
    cap_file_dir = '/root/Cylon-Raider-Lite/logs'
    capture_Interface = 'wlan1mon'
    dev_null = open(os.devnull,'w')

    # run airodump-ng on the foreground
    cmd_String = "airodump-ng wlan1mon -a --write %s/%s_monitor_mode_capture.cap" % (cap_file_dir, timestr)
    cmd_String = "airodump-ng -a --write %s/%s_monitor_mode_capture.csv  --write-interval 5 --output-format csv wlan1mon" % (cap_file_dir, timestr)
    print cmd_String
    os.system(cmd_String)# we should open this in a new box to avoid disrupting the process
    os.system('cat /root/Cylon-Raider-Lite/logs/*.csv > /sdcard/Cylon_Raider_Recon.txt')
    os.system('cat /root/Cylon-Raider-Lite/logs/*.csv > /root/Cylon_Raider_Recon.txt')
    return

def thread_2():
    # import variables
    cap_file_dir = '/root/Cylon-Raider-Lite/logs'
    capture_Interface = 'wlan1mon'
    dev_null = open(os.devnull,'w')

    # run the hidden network sniffer in the background
    proc_String = "python /root/Cylon-Raider-Lite/sniffHidden.py"
    # p = subprocess.Popen(proc_String, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    # p = Popen(proc_String, shell=True, stderr=STDOUT, stdout=dev_null)
    os.system(proc_String)
    # hidden_scanner_output = p.communicate()
    # print hidden_scanner_output
    # return hidden_scanner_output
    return


x = threading.Thread(name='thread_1', target=thread_1)
y = threading.Thread(name='thread_2', target=thread_2)

x.start()
y.start()

if KeyboardInterrupt:
    x.terminate()
    y.terminate()

# #!/usr/bin/env python
# # coding=UTF-8
#
# import os
# import socket
# import operator
# # #from termcolor import colored
# import sys
# import time
# from subprocess import *
# from subprocess import Popen
# from subprocess import PIPE
# import threading
#
# cap_file_dir = '/root/Cylon-Raider-Lite/logs'
# capture_Interface = 'wlan1mon'
# dev_null = open(os.devnull,'w')
# # os.system('cat /root/Cylon-Raider-Lite/banner_airmon.txt')
#
# # sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
#
# # capture_Interface = str(raw_input("Enter the capture INTERFACE that was revealed to you in AIRMON: "))
# # capture_Interface = CrackHead.airodump_String #For some reason this isnt working, it was supposed to import airodump_String from the first module
# timestr = time.strftime("%Y%m%d-%H%M%S")
# proc_String = "python /root/Cylon-Raider-Lite/sniffHidden.py"
#
# cmd_String = "airodump-ng wlan1mon -a --write %s/%s_monitor_mode_capture.cap" % (cap_file_dir, timestr)
# print cmd_String
# os.system(cmd_String)# we should open this in a new box to avoid disrupting the process
# while os.system(cmd_String) == True:
#     proc_String = "python /root/Cylon-Raider-Lite/sniffHidden.py"
#     # p = subprocess.Popen(proc_String, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
#     p = Popen(proc_String, shell=True, stderr=STDOUT, stdout=dev_null)
#
#     hidden_scanner_output = p.communicate()
#     print hidden_scanner_output
#     try:
#         subprocess.check_call(proc_String)
#         print 'SUCCESS: The process exited with code 0'
#     except subprocess.CalledProcessError:
#         print 'ERROR: There was an error - command exited with non-zero code'
#         print subprocess.CalledProcessError
